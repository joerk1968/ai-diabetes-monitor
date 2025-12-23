import os
from data.monitor_loop import run_monitoring_loop

if __name__ == "__main__":
    # Safety kill switch
    if os.getenv("MONITOR_ENABLED", "true").lower() != "true":
        print("🛑 Monitoring disabled by MONITOR_ENABLED")
        exit(0)

    print("🩺 Diabetes glucose monitor started (Railway-ready)")
    
    run_monitoring_loop(
        interval_seconds=5
    )
