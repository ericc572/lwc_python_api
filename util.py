import subprocess
import os

def run_sub_process(accountName):
  subprocess.run(['sh','fire_scraper', accountName], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
