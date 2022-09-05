from_id = 1
to_id = 100
username = "username"
host = "x.x.x.x"
cmd = "scp {} %s@%s:/jigsaw.diew.app/pass/" % (username, host)

gen = " ".join([ "{}.json".format(i) for i in range(from_id, to_id+1) ])
print(cmd.format(gen))
