import subprocess
import os

def run_sub_process(accountName):
  print("Running subprocess to fire shell script")
  subprocess.run(['sh','fire_scraper', accountName])
