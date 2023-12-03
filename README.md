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

To restore, run

```
./kde-window-status-restore-restore.sh
```

## Related

[konsole-session-restore](https://github.com/Kelvin-Ng/konsole-session-restore): A set of scripts that save and restore Konsole sessions in KDE Plasma. Can be used together with this script.

