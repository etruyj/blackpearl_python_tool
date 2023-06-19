# CreateShares.py


def cifs(blackpearl, name, volume, mount_point, read_only, service_id, logbook):
    path = mount_point[7:] # Path is mount_point without the /export

    return blackpearl.createCifsShare(name, path, volume, read_only, service_id, logbook)

def nfs(blackpearl, comment, volume, mount_point, access_control, service_id, logbook):
    path = "/" # Path can only be root

    return blackpearl.createNfsShare(comment, volume, mount_point, path, access_control, service_id, logbook)

def vail(blackpearl, name, service_id, volume_id, logbook):
    # This function exists to have a similar path to the other two functions.

    return blackpearl.createVailShare(name, service_id, volume_id, logbook)
