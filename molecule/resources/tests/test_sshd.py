"""Role testing files using testinfra."""


import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_sshd_is_installed(host):
    sshd = host.package("openssh-server")
    assert sshd.is_installed


def test_sshd_running_and_enabled(host):
    sshd = host.service("sshd")
    assert sshd.is_running
    assert sshd.is_enabled


def test_ssh_user(host):
    assert host.user("sshd").exists
