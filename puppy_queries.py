def queryPuppiesOrderedAlphabetically():
    list = session.query(Puppy).order_by(Puppy.name).all()
    for puppy in list:
        print puppy.name
    return list

def queryPuppiesSixMonthsOrYounger():
    six_months_ago = datetime.date.today - date.timedelta(6 * 365/12)
    session.query(Puppy).filterby(Puppy.dateOfBirth > six_months_ago).order_by(Puppy.dateOfBirth).all()

def queryPuppiesByWeightAscending():
    return session.query(Puppy).order_by(weight).all()

def queryPuppiesGroupByShelter():
    return session.query(Puppy, Shelter).join(Shelter).order_by(Puppy.shetler_id).all()


