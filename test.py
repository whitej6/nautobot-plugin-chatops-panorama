import requests
import pdb
import os

HOST = os.getenv("PALO_HOST")
USERNAME = os.getenv("PALO_USERNAME")
PASSWORD = os.getenv("PALO_PASSWORD")

def get_api_key(host, username, password):
    key = ""
    try:
        with open("SECRETS.DONTLOOKATTHISFILE", "r") as f:
            key = f.read()
    except:
        pass

    if not key:   
        url = f"https://{host}/api/?type=keygen&user={username}&password={password}"
        key = requests.get(url, verify=False).text.split("<key>")[1].split("</key>")[0]

        with open("SECRETS.DONTLOOKATTHISFILE", "w") as f:
            f.write(key)
    return key

def create_capture_filter(host, api_key, interface, source="0.0.0.0", destination="0.0.0.0", non_ip="exclude", ipv6_only="no"):
    capture_filter = f"""
    <debug>
        <dataplane>
            <packet-diag>
            <set>
                <filter>
                <index>
                    <entry name="1">
                    <match>
                        <ingress-interface>{interface}</ingress-interface>
                        <source>{source}</source>
                        <destination>{destination}</destination>
                        <non-ip>{non_ip}</non-ip>
                        <ipv6-only>{ipv6_only}</ipv6-only>
                    </match>
                    </entry>
                </index>
                </filter>
            </set>
            </packet-diag>
        </dataplane>
    </debug>
    """
    url = f"https://{host}/api/?key={api_key}&type=op&cmd={capture_filter}"
    response = requests.post(url, data=capture_filter, verify=False)
    print(response.text)

def create_packet_capture(host, api_key):
    url = f"https://{host}/api/?key={api_key}&type=log&log-type-traffic"
    response = requests.get(url, verify=False)
    print(response.text)

def start_packet_capture():
    pass

def stop_packet_capture():
    pass

def get_packet_capture():
    pass

def delete_packet_capture():
    pass

def delete_capture_filter():
    pass


if __name__ == "__main__":
    api_key = get_api_key(HOST, USERNAME, PASSWORD)
    #create_packet_capture(HOST, api_key)

    # create a filter"""
    create_capture_filter(HOST, api_key, "ethernet1/1")

    # create a capture

    # start a capture

    # after a set amount of time stop capture

    # get capture file

    # delete capture

    # delete filter