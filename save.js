var res = {}

const clients = workspace.clientList();
for (var i = 0; i < clients.length; i++) {
    if (clients[i].desktop == -1) {
        continue;
    }
    one_res = {'activities': clients[i].activities, 'desktop': clients[i].desktop};
    res[clients[i].caption] = one_res;
}

res_str = JSON.stringify(res);

callDBus('org.kde.KWin.Script.KdeWindowStatusRestore', '/callback', 'org.kde.kwin.Script', 'Save', res_str)

