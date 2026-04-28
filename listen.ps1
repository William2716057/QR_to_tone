param(
    [int]$DurationSeconds = 5,
    [string]$OutputPath = "$PWD\recording.wav"
)

Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public class WaveRecorder {
    [DllImport("winmm.dll", EntryPoint="mciSendStringA", CharSet=CharSet.Ansi)]
    public static extern int mciSendString(string lpstrCommand, string lpstrReturnString, int uReturnLength, int hwndCallback);
}
"@

Write-Host "Output: $OutputPath"

[WaveRecorder]::mciSendString("open new Type waveaudio Alias recsound", "", 0, 0) | Out-Null
[WaveRecorder]::mciSendString("set recsound channels 2 bitspersample 16 samplespersec 44100", "", 0, 0) | Out-Null
[WaveRecorder]::mciSendString("record recsound", "", 0, 0) | Out-Null

for ($i = $DurationSeconds; $i -gt 0; $i--) {
    Write-Host "`r[REC] Recording... $i seconds remaining  " -NoNewline
    Start-Sleep -Seconds 1
}


Write-Host "`r[DONE] Recording saved"

[WaveRecorder]::mciSendString("stop recsound", "", 0, 0) | Out-Null
[WaveRecorder]::mciSendString("save recsound `"$OutputPath`"", "", 0, 0) | Out-Null
[WaveRecorder]::mciSendString("close recsound", "", 0, 0) | Out-Null

