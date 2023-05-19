import json
import os

def new_apointment(id, today, events_yesterday):
    """TODO: FINISH IT
    The most complex algorithm in the system would be the planning of the apointments to be as cheap and safe as possible"""
    # Finding the human
    ids = id.split()
    if (ids[0] in os.listdir("dataset\people")):
        if (ids[1] in os.listdir("dataset/people/" + ids[0])):
            if (ids[2] + ".json" in os.listdir("dataset/people/" + ids[0] + "/" + ids[1])):
                data = json.load(open("dataset/people/" + ids[0] + "/" + ids[1] + "/" + ids[2] + ".json", "r"))
            else:
                return("ERROR; There is no such an ID in the system!;")
        else:
            return("ERROR; There is no such an ID in the system!;")
    else:
        return("ERROR; There is no such an ID in the system!;")

    pass


def cancel_apointment(human_id, apointment_id):
    """If a user wats to, they can cancel an apointment, but its not recomennded."""

    ids = human_id.split()
    # Finding the human
    if (ids[0] in os.listdir("dataset\people")):
        if (ids[1] in os.listdir("dataset/people/" + ids[0])):
            if (ids[2] + ".json" in os.listdir("dataset/people/" + ids[0] + "/" + ids[1])):
                data = json.load(open("dataset/people/" + ids[0] + "/" + ids[1] + "/" + ids[2] + ".json", "r"))
            else:
                return("ERROR; There is no such an ID in the system!;")
        else:
            return("ERROR; There is no such an ID in the system!;")
    else:
        return("ERROR; There is no such an ID in the system!;")
    
    #finding the apointment
    for apointment in data["upcomming_scans"]:
        if (apointment_id == apointment["id"]):
            data["upcomming_scans"].remove(apointment) # deleting it
            return("SUCCESS!;")


def set_schedule(id, scan_type, freq, range):
    """The ID of the human you want to set a schedule, the TYPE of scan you want to schedule, the FREQuency mesured in days, 
    and the maximum RANGE you allow for the system to put the patient away from the ideal date"""
    ids = id.split()


    # Finding the human
    if (ids[0] in os.listdir("dataset\people")):
        if (ids[1] in os.listdir("dataset/people/" + ids[0])):
            if (ids[2] + ".json" in os.listdir("dataset/people/" + ids[0] + "/" + ids[1])):
                data = json.load(open("dataset/people/" + ids[0] + "/" + ids[1] + "/" + ids[2] + ".json", "r"))
            else:
                return("ERROR; There is no such an ID in the system!;")
        else:
            return("ERROR; There is no such an ID in the system!;")
    else:
        return("ERROR; There is no such an ID in the system!;")
    
    #setting
    sq = data["scan_sqedule"]
    if (scan_type in sq.keys()):#creating schedule
        sq[scan_type]["freq"] = freq
        sq[scan_type]["range"] = range

    else:
        sq[scan_type] = {"freq": freq, "range":range} # changing schedule


def get_history(id, past, event_type):
    """the ID of the human you intrested in
        the SIZE of the data array you want to get (if the dataset has less item than the SIZE, it gives back the whole array)
        the TYPE of the events you intrested in"""
    ids = id.split()

    # Finding the human
    if (ids[0] in os.listdir("dataset\people")):
        if (ids[1] in os.listdir("dataset/people/" + ids[0])):
            if (ids[2] + ".json" in os.listdir("dataset/people/" + ids[0] + "/" + ids[1])):
                data = json.load(open("dataset/people/" + ids[0] + "/" + ids[1] + "/" + ids[2] + ".json", "r"))[event_type]
            else:
                return("ERROR; There is no such an ID in the system!;")
        else:
            return("ERROR; There is no such an ID in the system!;")
    else:
        return("ERROR; There is no such an ID in the system!;")

    res = ""
    for x in data:
        for y in x.keys():
            res += str(x[y]) + ";"
        res = res[:-1] + "|"
    res = res[:-1]
    
    return(res)


def register_event(id, date, place, event_type, description):
    """the ID of the human who was (or will be) treated,
      the DATE and PLACE where the treatment was (or will be) made,
      the TYPE of the event (treatment or upcomming_scan or past_scan)
      the DESCRIPTION of the event"""
    template = {
        "date": date,
        "place": place,
        "description": description
    }

    ids = id.split()

    # Finding the human
    if (ids[0] in os.listdir("dataset\people")):
        if (ids[1] in os.listdir("dataset/people/" + ids[0])):
            if (ids[2] + ".json" in os.listdir("dataset/people/" + ids[0] + "/" + ids[1])):
                data = json.load(open("dataset/people/" + ids[0] + "/" + ids[1] + "/" + ids[2] + ".json", "r"))
                data[event_type].append(template)
                json.dump(data, open("dataset/people/" + ids[0] + "/" + ids[1] + "/" + ids[2] + ".json", "w"))
                return("SUCCESS; The event has been added")
            else:
                return("ERROR; There is no such an ID in the system!;")
        else:
            return("ERROR; There is no such an ID in the system!;")
    else:
        return("ERROR; There is no such an ID in the system!;")


def register_new_location(name, distance_vec, events):
    """Manually register places where medical treatment and scans can be finalised. 
    This would be usefull in the future expansions of the project, to consider the closes places for every people when planning the apointments."""

    obj = json.load(open("dataset\locations.json", "r"))
    if (name in obj.keys()):
        return("ERROR; this location is already exist in the dataset!;")
    else:
        obj[name] = {"distance_vector": distance_vec, "possible_events": events}
        return("SUCCESS; this location is now exist in the dataset!;")


def register_patient(id, name, adress):
    """the ID, name and adress of the human being registered"""
    ids = id.split()
    template = {
        "personal_data": {
            "name": name,
            "adress": adress
        },
        "treatments": [],
        "upcomming_scans": [],
        "past_scans": [],
        "scan_sqedule": {}
    }
    # Finding the human
    if (ids[0] in os.listdir("dataset\people")):
        if (ids[1] in os.listdir("dataset/people/" + ids[0])):
            if (ids[2] + ".json" in os.listdir("dataset/people/" + ids[0] + "/" + ids[1])):
                return("ERROR; The patient is already registered!;")
            else:
                json.dump(template, open("dataset/people/" + ids[0] + "/" + ids[1] + "/" + ids[2] + ".json", "w"))
                return("SUCCESS; The patient has been registered!;")
        else:
            os.mkdir("dataset/people/" + ids[0] + "/" + ids[1])
            json.dump(template, open("dataset/people/" + ids[0] + "/" + ids[1] + ".json", "w"))
            return("SUCCESS; The patient has been registered!;")
    else:
        os.mkdir("dataset/people/" + ids[0])
        os.mkdir("dataset/people/" + ids[0] + "/" + ids[1])
        json.dump(template, open("dataset/people/" + ids[0] + "/" + ids[1] + "/" + ids[2] + ".json", "w"))
        return("SUCCESS; The patient has been registered!;")
    

def register_appointment(human_id, apointment_id, date, place, desc):
    """Manual method to create an apointment"""

    # Finding the human
    ids = human_id.split()
    if (ids[0] in os.listdir("dataset\people")):
        if (ids[1] in os.listdir("dataset/people/" + ids[0])):
            if (ids[2] + ".json" in os.listdir("dataset/people/" + ids[0] + "/" + ids[1])):
                data = json.load(open("dataset/people/" + ids[0] + "/" + ids[1] + "/" + ids[2] + ".json", "r"))
            else:
                return("ERROR; There is no such an ID in the system!;")
        else:
            return("ERROR; There is no such an ID in the system!;")
    else:
        return("ERROR; There is no such an ID in the system!;")
    
    data["upcomming_scans"].append({"id": apointment_id, "date": date,
                                    "place": place, "description": desc})
    
    json.dump(data, open("dataset/people/" + ids[0] + "/" + ids[1] + "/" + ids[2] + ".json", "w")) # saving

        
if __name__ == '__main__':
    # Setting up some testing data
    print(register_patient("153 365 568", "Molnár Tamás", "Szeged"))
    print(register_appointment("153 365 568", "123", "202209191430", "Szeged", "lung_scan"))
    print(register_appointment("153 365 568", "124", "202209191530", "Szeged", "eye_scan"))
    print(register_appointment("153 365 568", "125", "202209191630", "Szeged", "heart_scan"))



    print(register_patient("154 375 598", "Hüvös Gergely", "Szeged"))
    print(register_appointment("154 375 598", "12", "202207191630", "Szeged", "leg_scan"))

    print(register_patient("169 369 369", "Németh Regő", "Szeged"))
    print(register_appointment("169 369 369", "123", "202209201430", "Szeged", "lung_scan"))

    print(register_patient("153 365 000", "Vashut Vojtech", "Szeged"))
    print(register_appointment("153 365 000", "123", "202209191435", "Szeged", "eye_scan"))


