from flask import Flask, request, jsonify
import scapy.all as scapy
from scapy.layers.l2 import ARP, Ether

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <body>
            <h1>Network Scanner</h1>
            <form id="scanForm" action="/scan" method="post">
                <label for="ipRange">Enter IP Range:</label>
                <input type="text" id="ipRange" name="ipRange" required>
                <button type="submit">Scan</button>
            </form>
        </body>
        </html>
    '''

@app.route('/scan', methods=['POST'])
def scan():
    ip_range = request.form.get('ipRange')
    
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)

    return jsonify(clients_list)

if __name__ == '__main__':
    app.run(debug=True)
