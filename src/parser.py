'''
logic for parsing SDIF (hy3) Hy-Tek file format
'''


from functools import singledispatch

# import line_types



from typing import Literal


_line_codes = Literal[

    # file info
    'A1',

    # meet info 
    'B1', # primary
    'B2', # secondary

    # team info
    'C1',
    'C2',
    'C3',

    # swimmer info
    'D1',

    # individual event info
    'E1', # entry
    'E2', # result

    # relay event info
    'F1',
    'F2',
    'F3',

    # split info
    'G1',

    # DQ info
    'H1',

]



# @singledispatch
# def parse_line(
#     code,
#     line,
#     *args,
#     **kwargs,
# ) -> list[str]:
#     ...


# @parse_line.register
# def _(
#     code: line_types.A1,
#     line: str,
# ) -> list[str]:
    
#     return [
#         line[0:2], # code
#         line[2:4], # idk
#         line[5:30].strip(), # description
#         line[30:46].strip(), # hy-tek
#         line[46:60].strip(), # software version
#         line[60:62], # month
#     ]



def parse_line(
    code: _line_codes,
    line: str,
) -> list[str]:

    if code == 'A1':
        return [
            line[0:2], # code
            line[2:4], # idk
            line[4:29].strip(), # description
            line[29:44].strip(), # hy-tek
            line[44:58].strip(), # software version
            line[58:60], # month
            line[60:62], # day
            line[62:66], # year
            line[66:73].strip(), # time
            line[73:75], # AM/PM
            line[75:128].strip(), # host team
        ]
    
    elif code == 'B1':
        return [
            line[0:2], # code
            line[2:47], # meet name
            line[47:92], # facility / location
            line[92:100], # start date
            line[100:108], # end date
            
            line[116:121], # altitude
            
        ]

    elif code == 'B2':
        return [
            line[0:2], # code

            line[93:95], # masters?
            
            line[96:98], # meet type
            line[98:99], # meet course
            
        ]

    elif code == 'C1':
        return [
            line[0:2], # code
            line[2:7], # team code
            line[7:37], # team name
            line[37:53], # team short name
            #missing state?
        ]

    elif code == 'C2':
        return [
            line[0:2], # code
            
        ]

    elif code == 'C3':
        return [
            line[0:2], # code
            
        ]

    elif code == 'D1':
        return [
            line[0:2], # code
            line[2:3], # gender
            line[3:8], # meet ID
            line[8:28], # last name
            line[28:48], # first name
            line[48:68], # nickname
            line[68:69], # middle initial
            line[69:83], # usa swimming ID
            line[83:88], # team ID
            line[88:90], # DOB month
            line[90:92], # DOB day
            line[92:96], # DOB month
            line[96:99], # age

        ]

    elif code == 'E1':
        return [
            line[0:2], # code
            # line[2:3], # gender
            line[3:8], # meet ID

            line[13:14], # event gender
            line[14:15], # event gender age
            line[15:21], # event distance
            line[21:22], # stroke
            line[22:25], # age min
            line[25:28], # age max
            line[32:38], # event fee
            line[38:42], # event number

            line[42:50], # converted entry time
            
            line[50:51], # event course
            line[51:59], # entry seed time
            line[59:60], # entry seed course

        ]

    elif code == 'E2':
        return [
            line[0:2], # code

            line[2:3], # event type
            line[3:11], # time
            line[11:12], # course 
            line[12:13], #time code
            line[13:15], # DQ code

            line[20:23], # heat
            line[23:26], # lane
            line[26:29], # heat place
            line[30:24], # overall place

            # skipping pad/plunger times

            line[87:95], # date


        ]

    elif code == 'F1':
        return [
            line[0:2], # code
        ]

    elif code == 'F2':
        return [
            line[0:2], # code
        ]
    
    elif code == 'F3':
        return [
            line[0:2], # code
        ]
    
    elif code == 'G1':
        result = [
            line[0:2], # code
            line[2:3], # event type
        ]

        for i in range(3, len(line), 11):

            split = [
                line[i:(i+2)].strip(), # split number
                line[(i+2):(i+10)].strip(), # split time
                line[(i+10):(i+11)].strip(), # split type? P/S/F
            ]

            if all(split):
                result += split
            else:
                break # skip remainder of line 
            
    

        return result


    elif code == 'H1':
        return [
            line[0:2], # code
            line[2:4], # DQ code
            line[4:].strip(), # DQ description
        ]
        
    else:
        raise NotImplementedError
        
    return





if __name__ == '__main__':

    ...


