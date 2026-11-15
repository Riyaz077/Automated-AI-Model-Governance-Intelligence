from src.aiguard.pipeline import run_monitoring
if __name__ == "__main__":
    report = run_monitoring()
    print("Monitoring completed.")
    print("Alerts:", report["alerts"])
