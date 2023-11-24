host = [["Workstaton.local","192.0.0.0"],["webserver.cloud","188.0.0.0"]]
with open('host.csv', 'w') as host_csv:
    writer = csv.writter(host_csv)
    writer.writerows(host)