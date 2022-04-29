import subprocess
import datetime as dt

def win_boottime() -> dt.datetime:
    """Boot datetime for windows

    Returns
    -------
    dt.datetime
        Boot datetime
    """
    secname = "System Boot Time"
    proc_systeminfo = subprocess.run("systeminfo", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True, encoding="utf8")
    list_sysinfo = proc_systeminfo.stdout.split("\n")
    
    for sysi in list_sysinfo:
        if secname in sysi:
            str_dt_boottime = sysi.split(":", 1)[1].strip()
            break
    
    dt_boottime = dt.datetime.strptime(str_dt_boottime, "%Y/%m/%d, %H:%M:%S")
    return dt_boottime

def uptime() -> dt.timedelta:
    """uptime for windows

    Returns
    -------
    dt.timedelta
        elapsed time from Boot Time
    """
    dt_boot = win_boottime()
    dt_now = dt.datetime.now()
    return dt_now - dt_boot

if __name__ == '__main__':
    btime = win_boottime()
    print(btime)
    print(btime.timestamp())
    # u_time = uptime()
    # print(u_time)