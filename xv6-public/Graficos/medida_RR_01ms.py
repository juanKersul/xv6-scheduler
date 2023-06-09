import numpy as np

# RR 0.1ms Escenario 2.
    #Notar las mediciones de iobench comienzan con io, las de cpu con cpu respectivamente.
    # 50 mediciones

# Caso 0: 1 iobench

io1_1_cpu0_01ms_RR = [781 ,767 ,815 ,812 ,773 ,787 ,811 ,818 ,760 ,855 ,
                      832 ,810 ,825 ,817 ,800 ,852 ,755 ,826 ,815 ,799 ,
                      782 ,750 ,1086,1195,1072,1144,910 ,733 ,984 ,899 ,
                      808 ,822 ,813 ,852 ,756 ,829 ,748 ,776 ,801 ,805 ,
                      760 ,825 ,804 ,785 ,817 ,845 ,919 ,899 ,830 ,796 ]


# Caso 1: 1 iobench 1 cpubench
        #Formato de nombre : cpu{nº cpus}_{nº de cpu medida}_io{nº de ios}_{nº de io medida}
cpu1_1_io1_1_01ms_RR = [0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0]

io1_1_cpu1_1_01ms_RR = [55 ,88 ,69 ,66 ,114,79 ,86 ,100,56 ,79 ,
                        104,80 ,120,62 ,82 ,96 ,59 ,74 ,80 ,73 ,
                        109,91 ,107,69 ,110,219,98 ,85 ,110,89 ,
                        114,61 ,82 ,58 ,76 ,87 ,69 ,103,74 ,81 ,
                        89 ,73 ,73 ,82 ,69 ,78 ,191,206,76 ,97 ]

# Caso 2: 1 iobench 2 cpubench
        #Formato de nombre : cpu{nº cpus}_{nº de cpu medida}_io{nº de ios}_{nº de io medida}
cpu2_1_io1_01ms_RR = [0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0]

cpu2_2_io1_01ms_RR = [0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0]

io1_1_cpu2_2_01ms_RR = [186,164,181,134,140,158,168,195,116,152,
                        141,150,151,164,156,112,197,145,152,167,
                        151,168,120,158,111,145,182,159,160,172,
                        144,151,146,149,191,145,151,154,175,152,
                        170,154,169,158,171,152,159,123,142,110]

# Caso 3: 1 cpubench
        #Formato de nombre : cpu{nº cpus}_{nº de cpu medida}_io{nº de ios}_{nº de io medida} si nº de io/cpu es cero no lo colocamos en el nombre.
cpu1_1_io0_01ms_RR = [0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0]

# Caso 4: 1 cpubench 2 iobench
        #Formato de nombre : cpu{nº cpus}_{nº de cpu medida}_io{nº de ios}_{nº de io medida}
cpu1_1_io2_2_01ms_RR = [0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0]

io2_1_cpu1_1_01ms_RR = [271,297,261,290,311,281,308,283,335,644,
                        654,740,622,333,314,501,513,782,460,300,
                        245,338,334,212,327,270,269,301,239,315,
                        343,275,351,303,362,353,253,362,276,290,
                        315,316,273,280,344,290,358,337,355,374]

io2_2_cpu1_1_01ms_RR = [384,339,302,309,321,353,297,357,424,383,
                        676,592,685,382,374,379,816,586,673,305,
                        296,355,298,279,363,276,305,396,350,255,
                        346,351,371,374,394,318,315,374,347,333,
                        334,311,318,383,340,382,367,365,425,329]

# Caso 5: 2 cpubench 2 iobench

cpu2_1_io2_2_01ms_RR = [0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0]

cpu2_2_io2_2_01ms_RR = [0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0]

io2_1_cpu2_2_01ms_RR = [41,58,53,78,70,71,80,65,53,58,
                        55,47,91,100,80,77,53,64,69,47,
                        92,71,61,75,63,104,62,59,108,60,
                        54,60,56,59,81,61,45,58,59,57,
                        72,48,56,60,66,68,53,70,20193]

io2_2_cpu2_2_01ms_RR = [171,199,220,204,218,189,215,210,230,190,
                        268,233,251,254,214,240,219,237,228,183,
                        232,159,214,200,188,245,244,183,186,216,
                        208,208,210,222,215,248,227,214,203,236,
                        230,213,192,202,232,223,202,228,236,208]

# Caso 6: 2 cpubench

cpu2_1_io0_01ms_RR = [0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0]

cpu2_2_io0_01ms_RR = [0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0]

# Caso 7: 2 iobench

io2_1_cpu0_01ms_RR = [358,377,374,530,372,358,367,470,346,483,
                      400,408,370,368,413,417,463,482,378,403,
                      345,389,383,390,529,360,403,330,353,441,
                      373,368,382,476,322,344,395,376,385,428,
                      418,396,373,437,440,420,338,391,361,383]

io2_2_cpu0_01ms_RR = [694,633,669,586,658,660,590,619,584,644,
                      620,652,614,659,618,619,669,693,628,569,
                      656,771,672,554,656,526,551,733,609,632,
                      618,572,623,557,614,566,666,626,569,767,
                      618,566,657,636,571,561,607,612,743,641]




def cpubench_01msRR():
    
    cpu2io0_01msRR = [(x+y)/2 for x,y in zip(cpu2_1_io0_01ms_RR,cpu2_2_io0_01ms_RR)]
    cpu2io1_01msRR = [(x+y)/2 for x,y in zip(cpu2_1_io1_01ms_RR,cpu2_2_io1_01ms_RR)]
    cpu2io2_01msRR = [(x+y)/2 for x,y in zip(cpu2_1_io2_2_01ms_RR,cpu2_2_io2_2_01ms_RR)]
    
    cpuμ_01msRR = [np.mean(cpu1_1_io0_01ms_RR),np.mean(cpu1_1_io1_1_01ms_RR),np.mean(cpu1_1_io2_2_01ms_RR),
                       np.mean(cpu2io0_01msRR),np.mean(cpu2io1_01msRR),np.mean(cpu2io2_01msRR)]

    return cpuμ_01msRR

    
def iobench_01msRR():
      
    io2cpu0_01msRR= [(x+y)/2 for x,y in zip(io2_1_cpu0_01ms_RR,io2_2_cpu0_01ms_RR)]
    io2cpu1_01msRR= [(x+y)/2 for x,y in zip(io2_1_cpu1_1_01ms_RR,io2_2_cpu1_1_01ms_RR)]
    io2cpu2_01msRR= [(x+y)/2 for x,y in zip(io2_1_cpu2_2_01ms_RR,io2_2_cpu2_2_01ms_RR)]
    
    ioμ_01msRR = [np.mean(io1_1_cpu0_01ms_RR),np.mean(io1_1_cpu1_1_01ms_RR),np.mean(io2cpu1_01msRR),
                np.mean(io2cpu0_01msRR),np.mean(io1_1_cpu2_2_01ms_RR),np.mean(io2cpu2_01msRR)]

    return ioμ_01msRR

cpuμ_01msRR = cpubench_01msRR()
ioμ_01msRR = iobench_01msRR()













