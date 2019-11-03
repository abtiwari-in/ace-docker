#!/usr/bin/env python
#import argparse
#import subprocess
from subprocess import Popen, PIPE, STDOUT
import os
import sys
import shlex
import time
import shutil

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = newPath

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)
"""
def shcmd(cmd, ignore_error=False):
    print('Doing:', cmd)
    ret = subprocess.call(cmd, shell=True)
    print('Returned', ret, cmd)
    if ignore_error == False and ret != 0:
        raise RuntimeError("Failed to execute {}. Return code:{}".format(
            cmd, ret))
    return ret
"""

def shcmd(cmd, ignore_error=False):
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    stdoutput = p.stdout.read().decode("utf-8")
    p.wait()
    if p.returncode == 0:
        cmd_res = {
            "returncode" : p.returncode,
            "stdout" : stdoutput
        }
    else:
        cmd_res = {
            "returncode" : p.returncode,
            "stderr" : p.stderr.read().decode("utf-8")
        }
    return cmd_res



def download_file_from_git(gitlab_base_url, gitlab_proj_id, gitlab_branch, gitlab_priv_token, file_path_to_download, filename_to_download, local_target_dir):
    print("in download_file_from_git : local_target_dir = ",local_target_dir)
    curl_auth_header = "'PRIVATE-TOKEN: " + gitlab_priv_token + "'"
#    cmd = "curl -H " + curl_auth_header + " -L " + gitlab_base_url + gitlab_proj_id + "/repository/files/" + file_path_to_download + "%2F"+ filename_to_download + "%2Eyaml/raw?ref=" + gitlab_branch + " > " + local_target_dir + "/" + filename_to_download + ".yaml"
	cmd = "curl -s https://" + gitlab_priv_token + "@" + gitlab_base_url + "/" + gitlab_proj_id + "/" + gitlab_branch + "/" + file_path_to_download + "/" + filename_to_download + ".bar" +  ">" + local_target_dir + "/" + filename_to_download + ".bar"
    print("my command: ", cmd)
    if not os.path.isdir(local_target_dir):
        os.makedirs(local_target_dir)
    """
    else:
        print("in else - is dir exists: ", os.path.isdir(local_target_dir))
        shutil.rmtree(local_target_dir)
        print("in else - is dir exists: ", os.path.isdir(local_target_dir))
        os.makedirs(local_target_dir)
    """

    #with cd(local_target_dir):
        #shcmd(cmd)
    download_file_from_git_res = shcmd(cmd)
    return download_file_from_git_res

"""
UNIT TESTING: Variables to be passed for the download function
"""
# Environment Variable
gitlab_base_url = os.environ['barfile-git-repo_base_url']
gitlab_proj_id = os.environ['barfile-git-repob_proj_id']
gitlab_branch = os.environ['barfile-git-repo_branch']
gitlab_priv_token = os.environ['barfile-git-repo_priv_token']
currentDirectory = os.getcwd()
local_target_dir = currentDirectory + "/sample/bars_aceonly" 
#local_target_dir = "/var/jenkins_home/workspace/ACEPipelineV2/sample/bars_aceonly"

# Runtime Variable
file_path_to_download = "bar"
filename_to_download = os.environ['barfilename']

download_file_from_git(gitlab_base_url, gitlab_proj_id, gitlab_branch, gitlab_priv_token, file_path_to_download, filename_to_download, local_target_dir)
