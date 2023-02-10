    """
    A simple function comparing datetime objects.

    Author: Andy Nash
    Date:   2022-12-30
    """
    import datetime
    from datetime import date
    from datetime import datetime



    def is_before(d1,d2):
        """
        Returns True if event d1 happens before d2.

        Values d1 and d2 can EITHER be date objects or datetime objects.
        If a date object, assume that it happens at midnight of that day.

        Parameter d1: The first event
        Precondition: d1 is EITHER a date object or a datetime object

        Parameter d2: The first event
        Precondition: d2 is EITHER a date object or a datetime object
        """
        # HINT: Check the type of d1 or d2. If not a datetime, convert it for comparison

        #if d1 happens before d2 and are the same type
        if type(d1) == type(d2):
            return d1 < d2

        #if not the same type
        elif type(d1) != type(d2):
            #check if d1 is a date, change to datetime
            #print('not same type')
            #print(type(d2))

            if type(d1) == date:
                #print('see this')
                convert_d1 = datetime.combine(d1,datetime.min.time())
                #print(convert_d1)
                    #then compare to d2
                return convert_d1 < d2


            if type(d2) == date:
                convert_d2 = datetime.combine(d2,datetime.min.time())
                #print('d2 was converted')
                #print(convert_d2)
                return d1 < convert_d2



    """
    d1 = date(2019,10,12)
    d2 = date(2019,10,15)
    d3 = datetime(2019,10,12,9,45,15)
    d4 = datetime(2019,10,12,10,15)


    is_before(d3,d1)
    """
