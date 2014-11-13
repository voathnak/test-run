import transmissionrpc
tc = transmissionrpc.Client('localhost', port=9091)
tc.get_torrents()