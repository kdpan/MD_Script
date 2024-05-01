import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

def rmsd_plot_single(rmsd_xvg,saved_fig,dpi=600):
    
    print(f'reading data from {rmsd_xvg}')
    with open(rmsd_xvg,'r') as f:
        rmsd_lines = f.readlines()
    
    time_list = []
    rmsd_list = []

    for line in tqdm(rmsd_lines,desc='process data for plot'):
        # 绘图单位为ns，原始文件单位为ps，所以要/1000
        time_list.append(float(line.split()[0])/1000)
        rmsd_list.append(float(line.split()[1]))

    print('Plotting...')
    plt.plot(time_list, rmsd_list)
    plt.xlabel("Time (ns)")
    plt.ylabel("RMSD (Å)")
    plt.title(f'Protein C{chr(945)} RMSD-Time Plot')
    plt.savefig(saved_fig,dpi=dpi)
    print(f'saved rmsd plot in {saved_fig}')

def rmsf_plot_single(rmsf_xvg,saved_fig,dpi=600):

    print(f'reading data from {rmsf_xvg}')
    with open(rmsf_xvg,'r') as f:
        rmsd_lines = f.readlines()
    
    res_list = []
    rmsf_list = []
    res_num = 1
    for line in tqdm(rmsd_lines,desc='process data for plot'):
        # 绘图单位为ns，原始文件单位为ps，所以要/1000
        res_list.append(res_num)
        rmsf_list.append(float(line.split()[1]))
        res_num += 1

    print('Plotting...')
    plt.plot(res_list, rmsf_list)
    plt.xlabel("Residue")
    plt.ylabel("Fluctuations (Å)")
    plt.title(f'Protein C{chr(945)} RMSF-Residue Plot')
    plt.savefig(saved_fig,dpi=dpi)
    print(f'saved rmsd plot in {saved_fig}')

def hbond_plot_single(hbond_num_xvg,saved_fig,dpi=600):
    with open(hbond_num_xvg) as f:
        lines = f.readlines()

    x = []
    y = []
    for line in lines:
        data = line.split()
        x.append(float(data[0])/1000)
        y.append(float(data[1]))

    plt.bar(x,y)
    plt.xlabel("Time (ns)")
    plt.ylabel('No. of H-Bond')
    plt.savefig(saved_fig,dpi=dpi)


if __name__ == '__main__':
    # 1.rmsd_plot one compound
    # rmsd_plot_single('data/rmsd.xvg','data/img/rmsd.png')

    # 2.rmsf_plot one compound
    # rmsf_plot_single('data/rmsf.xvg','data/img/rmsf.png')

    # 3.Hbond plot one compound
    hbond_plot_single('data/bond_num.xvg','data/img/hbond.png')

