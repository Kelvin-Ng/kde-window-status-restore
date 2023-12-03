callDBus('org.kde.KWin.Script.KdeWindowStatusRestore', '/callback', 'org.kde.kwin.Script', 'Read', function (res_str) {
    const res = JSON.parse(res_str);
    const clients = workspace.clientList();
    for (var i = 0; i < clients.length; i++) {
        if (clients[i].desktop == -1) {
            continue;
        }

        if (clients[i].caption in res) {
            clients[i].activities = res[clients[i].caption].activities;
            clients[i].desktop = res[clients[i].caption].desktop;
        }
    }

    callDBus('org.kde.KWin.Script.KdeWindowStatusRestore', '/callback', 'org.kde.kwin.Script', 'Finish');
})
