# KDE Window Status Restore

This is a set of scripts that save and restore statuses of windows in KDE Plasma.
This is useful in Wayland session because Wayland does not have session restore yet.

Note that the scripts only save and restore *statuses* - the actual windows are not opened by the restore script.
We still rely on the applications themselves to reopen the windows.
Many modern applications can already do that, like Firefox.
After the windows are reopened, you can run the restore script to restore their statuses.

Currently, only activities and desktops are restored.

## Usage

To save statuses, run

```
./kde-window-status-restore-save.sh
```
This can be configured to run automatically on logout by adding it to System Settings > Startup and Shutdown > Autostart > Add > Add Logout Script.

To restore, run

```
./kde-window-status-restore-restore.sh
```
This can be binded to a keyboard shortcut (e.g. Super + Shift + R) which can be used to restore the windows after they have all been opened.

## Related

[konsole-session-restore](https://github.com/Kelvin-Ng/konsole-session-restore): A set of scripts that save and restore Konsole sessions in KDE Plasma. Can be used together with this script.

## Known Issues

### Cannot autorun

Currently I have not found a way to make the script work with autorun (automatically save statuses at logout) because the script may start after some applications close, and these applications will not be saved. Contribution is welcomed if you have a way to ensure the execution order between the scripts and the applications.

Also, because this script relies on the caption to identify the windows, the restoring script can only run after the captions stablize. However, applications like Firefox will first reopen the windows with default captions and slowly update the captions as the tabs load. Contribution is welcomed if you have a way to programmatically run the restoring script after the captions stablize.

### Conflicting captions

As we identify windows with captions, windows that have the same captions will not be restored correctly.

