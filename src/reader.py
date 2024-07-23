'''
logic for reading hy3 file
'''

from parser import parse_line



_path = 'sample_data/meet-results-sand-rtb-summer-championship-july-2024-12jul2024-001/Meet Results-SAND RTB Summer Championship - July 2024-12Jul2024-001.hy3'



def main():


    with open(_path, 'r') as f:
        for i, line in enumerate(f):
            if i < 10:
                code = line[:2]
                result = parse_line(code, line)
                print(result)







if __name__ == '__main__':
    
    main()