"""
M-1 MOTORWAY MASTER SIMULATION & BENCHMARK RUNNER
=================================================
Runs all Python simulation modules, statistical tests, advanced ML suites,
and figure generation in sequence.
"""

import os
import sys
import subprocess
import time

def run_script(script_path, desc):
    print("\n" + "=" * 75)
    print(f"[{time.strftime('%H:%M:%S')}] RUNNING: {desc}")
    print(f"File: {script_path}")
    print("=" * 75)
    res = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"ERROR running {script_path}:\n{res.stderr}")
        return False
    else:
        print(res.stdout.strip())
        return True

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    
    scripts = [
        (os.path.join(root, "controllers", "m1_real_physics_engine.py"), "Hardened Real Physics & Pacejka Engine"),
        (os.path.join(root, "controllers", "m1_advanced_ml_suite.py"), "Advanced Machine Learning & Explainable AI (XAI) Suite"),
        (os.path.join(root, "controllers", "m1_multi_algorithm_benchmark.py"), "Multi-Algorithm Cybersecurity & Controller Benchmark"),
        (os.path.join(root, "controllers", "m1_comprehensive_statistical_suite.py"), "ANOVA & Rigorous Hypothesis Testing Suite"),
        (os.path.join(root, "controllers", "m1_annual_digital_twin_engine.py"), "365-Day Big Data Simulation Engine (38.95M Trips)"),
        (os.path.join(root, "controllers", "m1_rsu_and_ev_engine.py"), "87 RSU Topology & EV Energy Engine"),
        (os.path.join(root, "generate_readme_figures.py"), "Publication Academic Figure Generation Suite (Figures 1-6)")
    ]

    print("=" * 75)
    print("STARTING FULL M-1 DIGITAL TWIN REPRODUCIBILITY PIPELINE")
    print("=" * 75)

    start_time = time.time()
    success_count = 0

    for script, desc in scripts:
        if os.path.exists(script):
            ok = run_script(script, desc)
            if ok:
                success_count += 1
        else:
            print(f"WARNING: Script not found: {script}")

    elapsed = time.time() - start_time
    print("\n" + "=" * 75)
    print(f"REPRODUCIBILITY PIPELINE FINISHED IN {elapsed:.2f} SECONDS")
    print(f"SUCCESS: {success_count}/{len(scripts)} Modules Executed Successfully")
    print("=" * 75)

if __name__ == "__main__":
    main()
