import csv
import matplotlib.pyplot as plt

CSV_PATH = "results/results.csv"

def read_rows():
    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            r["Size"] = int(r["Size"])
            r["Time (sec)"] = float(r["Time (sec)"])
            r["Memory (bytes)"] = float(r["Memory (bytes)"])
            rows.append(r)
    return rows

def save_plot(rows, metric, prefix):
    datasets = sorted(set(r["Dataset"] for r in rows))
    algorithms = sorted(set(r["Algorithm"] for r in rows))

    for ds in datasets:
        plt.figure()
        for algo in algorithms:
            part = [r for r in rows if r["Dataset"] == ds and r["Algorithm"] == algo]
            part.sort(key=lambda x: x["Size"])
            xs = [r["Size"] for r in part]
            ys = [r[metric] for r in part]
            plt.plot(xs, ys, marker="o", label=algo)

        plt.xlabel("Input size (n)")
        plt.ylabel(metric)
        plt.title(f"{metric} vs n ({ds})")
        plt.legend()
        plt.tight_layout()
        out = f"results/{prefix}_{ds}.png"
        plt.savefig(out, dpi=200)
        plt.close()
        print("Saved:", out)

if __name__ == "__main__":
    rows = read_rows()
    save_plot(rows, "Time (sec)", "time")
    save_plot(rows, "Memory (bytes)", "memory")
    print("✅ Done. PNG graphs saved in results/ folder.")
