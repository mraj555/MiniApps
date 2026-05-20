import subprocess

data = (
    subprocess.check_output(["netsh", "wlan", "show", "profiles"])
    .decode("utf-8", errors="backslashreplace")
    .split("\n")
)

profiles = []

for i in data:
    if "All User Profile" in i:
        profiles.append(i.split(":")[1][1:-1])

for i in profiles:
    try:
        result = (
            subprocess.check_output(
                ["netsh", "wlan", "show", "profile", f"name={i}", "key=clear"]
            )
            .decode("utf-8", errors="backslashreplace")
            .split("\n")
        )

        results = []

        for b in result:  # ✅ iterate `result` not `results`
            if "Key Content" in b:
                results.append(b.split(":")[1][1:-1])

        try:
            print("{:<30}| {:<}".format(i, results[0]))
        except:
            print("{:<30}| {:<}".format(i, "No Password"))
    except:
        print("{:<30}| {:<}".format(i, "Error Occurred"))
