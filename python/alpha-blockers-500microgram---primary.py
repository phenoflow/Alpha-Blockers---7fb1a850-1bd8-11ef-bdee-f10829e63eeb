# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2024.

import sys, csv, re

codes = [{"code":"44553","system":"gprdproduct"},{"code":"1455","system":"gprdproduct"},{"code":"24369","system":"gprdproduct"},{"code":"4111","system":"gprdproduct"},{"code":"41652","system":"gprdproduct"},{"code":"35312","system":"gprdproduct"},{"code":"35058","system":"gprdproduct"},{"code":"53084","system":"gprdproduct"},{"code":"34080","system":"gprdproduct"},{"code":"36282","system":"gprdproduct"},{"code":"51665","system":"gprdproduct"},{"code":"35466","system":"gprdproduct"},{"code":"35925","system":"gprdproduct"},{"code":"54497","system":"gprdproduct"},{"code":"41651","system":"gprdproduct"},{"code":"43547","system":"gprdproduct"},{"code":"42462","system":"gprdproduct"},{"code":"58517","system":"gprdproduct"},{"code":"14932","system":"gprdproduct"},{"code":"31109","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('alpha-blockers-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["alpha-blockers-500microgram---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["alpha-blockers-500microgram---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["alpha-blockers-500microgram---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
