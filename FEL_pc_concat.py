

def concat_xvg_gy_rm(xvg_gy,xvg_rm,xvg_cat):
    with open(xvg_gy) as f:
        gy_lines = f.readlines()
    
    gy_data = []
    for l in gy_lines:
        if l.startswith('@') or l.startswith('#'):
            continue
        if l:
            gy_data.append(l)
    
    with open(xvg_rm) as f:
        rm_lines = f.readlines()

    rm_data = []
    for l in gy_lines:
        if l.startswith('@') or l.startswith('#'):
            continue
        if l:
            rm_data.append(l)

    with open(xvg_cat,'w') as f:
        for i in range(len(gy_data)):
            gy_time = int(gy_data[i].split()[0])
            gy = float(gy_data[i].split()[1])
            rm_time = float(rm_data[i].split()[0])
            rm = float(rm_data[i].split()[1])
            if gy_time == rm_time:
                f.write(f'{gy_time}\t{gy}\t{rm}\n')

if __name__ == "__main__":
    # 1. get sham.xvg file from gyrate.xvg and rmsd_xvg file
    concat_xvg_gy_rm('data/FEL_gyrate.xvg','data/FEL_rmsd.xvg','data/sham.xvg')
     