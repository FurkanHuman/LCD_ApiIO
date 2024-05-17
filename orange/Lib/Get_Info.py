import psutil
import re
import subprocess


class Get_Info:
    def __init__(self) -> None:
        pass

    async def get_ip(self, interface: str):
        result = subprocess.run(
            ['ifconfig', interface], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        match = re.search(
            r'inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', output)
        if match:
            return match.group(1)
        else:
            return "Bağlı Değil"

    async def get_cpu_temperature(self):
        result = subprocess.run(['cputemp'], capture_output=True, text=True)
        output = result.stdout.strip()
        temperature = float(output.split(':')[1].strip()[:-4])
        return temperature

    def get_running_docker_containers(self):
        try:
            result = subprocess.run(
                ['docker', 'ps', '-q'], stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8').strip()
            if output:
                return len(output.split('\n'))
            else:
                return 0
        except Exception as e:
            print("Error:", e)
            return -1

    def get_ram_usage(self):
        return (f"{((psutil.virtual_memory().used/1024)/1024)/1024:.2f}GB")

    def get_cpu_usage(self):
        cpu_usage = psutil.cpu_percent()
        return f"{cpu_usage}"
