from zk import ZK, const



def addUser(ip, port, uid, name, privilege, password, group_id, user_id, fingerprints):
    conn = None
    zk = ZK(ip, port=port, timeout=5, password=password, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        # another commands will be here!
        # Add User
        conn.set_user(uid, name, privilege, password, group_id, user_id)    
        conn.enable_device()
        return True, f"User {name} added successfully"
    except Exception as e:
        return False, f"Error adding user {name} to device {ip}: {e}"
    finally:
        if conn:
            conn.disconnect()
            print(f"Disconnected from device {ip}")
            


def addFingerprintFromReader(ip, port, password, uid, fid, valid, template):
    conn = None
    zk = ZK(ip, port=port, timeout=5, password=password, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        # another commands will be here!
        # Add Fingerprint
        conn.save_user_template(uid, fid, valid, template)
        conn.enable_device()
        return True, f"Fingerprint {fid} added successfully"
    except Exception as e:
        return False, f"Error adding fingerprint {fid} to user {uid} on device {ip}: {e}"
    finally:
        if conn:
            conn.disconnect()
            print(f"Disconnected from device {ip}")


def getAttendance(ip, port, password):
    conn = None
    zk = ZK(ip, port=port, timeout=5, password=password, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        # another commands will be here!
        # Get Attendance
        attendance = conn.get_attendance()
        conn.enable_device()
        return True, attendance
    except Exception as e:
        return False, f"Error getting attendance from device {ip}: {e}"
    finally:
        if conn:
            conn.disconnect()
            print(f"Disconnected from device {ip}")
            
            
def getUsers(ip, port, password):
    conn = None
    zk = ZK(ip, port=port, timeout=5, password=password, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        # another commands will be here!
        # Get Users
        users = conn.get_users()
        conn.enable_device()
        return True, users
    except Exception as e:
        return False, f"Error getting users from device {ip}: {e}"
    finally:
        if conn:
            conn.disconnect()
            print(f"Disconnected from device {ip}")
            
def deleteUser(ip, port, password, uid):
    conn = None
    zk = ZK(ip, port=port, timeout=5, password=password, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        # another commands will be here!
        # Delete User
        conn.delete_user(uid)
        conn.enable_device()
        return True, f"User {uid} deleted successfully"
    except Exception as e:
        return False, f"Error deleting user {uid} from device {ip}: {e}"
    finally:
        if conn:
            conn.disconnect()
            print(f"Disconnected from device {ip}")
            
def deleteFingerprint(ip, port, password, uid, fid):
    conn = None
    zk = ZK(ip, port=port, timeout=5, password=password, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        # another commands will be here!
        # Delete Fingerprint
        conn.delete_user_template(uid, fid)
        conn.enable_device()
        return True, f"Fingerprint {fid} deleted successfully"
    except Exception as e:
        return False, f"Error deleting fingerprint {fid} from user {uid} on device {ip}: {e}"
    finally:
        if conn:
            conn.disconnect()
            print(f"Disconnected from device {ip}")