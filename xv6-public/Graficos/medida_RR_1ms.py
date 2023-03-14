import numpy as np

# RR 1ms Escenario 1.
    #Notar las mediciones de iobench comienzan con io, las de cpu con cpu respectivamente.
    # 50 mediciones

# Caso 0: 1 iobench

io1_1_cpu0_1ms_RR = [3069, 2925, 3024, 2973, 3132, 3068, 2980, 2918, 2902, 3006,
                    3033, 2947, 2914, 2972, 3053, 3008, 3092, 2932, 3047, 3024,
                    2757, 2960, 2925, 2979, 2909, 2986, 2986, 2895, 3062, 2944,
                    3036, 2996, 2858, 2886, 2952, 2906, 3059, 2969, 2853, 3107,
                    2898, 2834, 2987, 3054, 3047, 2993, 2964, 2879, 2918, 3004]


# Caso 1: 1 iobench 1 cpubench
        #Formato de nombre : cpu{nº cpus}_{nº de cpu medida}_io{nº de ios}_{nº de io medida}
cpu1_1_io1_1_1ms_RR = [21, 20, 20, 20, 20, 19, 20, 20, 20, 20,
                       20, 20, 20, 20, 20, 20, 20, 19, 19, 19,
                       20, 19, 20, 19, 19, 19, 19, 19, 20, 20,
                       21, 20, 20, 19, 20, 19, 20, 20, 19, 20,
                       20, 19, 20, 19, 20, 20, 20, 20, 20, 20]

io1_1_cpu1_1_1ms_RR = [1012, 1061, 1027, 1038, 1069, 1045, 1051, 1060, 1042, 1057,
                       1041, 1070, 1062, 1068, 1061, 1095, 1053, 1043, 1060, 1051,
                       1044, 1051, 1100, 1057, 1058, 1081, 1081, 1045, 1042, 1063,
                       1069, 1033, 1047, 1064, 1085, 1058, 1064, 1069, 1063, 1040,
                       1046, 1060, 1085, 1067, 1036, 1090, 1055, 1067, 1047, 1100]

# Caso 2: 1 iobench 2 cpubench
        #Formato de nombre : cpu{nº cpus}_{nº de cpu medida}_io{nº de ios}_{nº de io medida}
cpu2_1_io1_1ms_RR = [15 ,16 ,16 ,16 ,16 ,16 ,16 ,16 ,16 ,16 ,
                     16 ,16 ,16 ,16 ,16 ,16 ,16 ,16 ,16 ,16 ,
                     17 ,17 ,16 ,16 ,17 ,17 ,16 ,16 ,16 ,16 ,
                     16 ,16 ,16 ,17 ,17 ,16 ,16 ,16 ,16 ,16 ,
                     16 ,17 ,16 ,16 ,16 ,16 ,16 ,17 ,16 ,16 ]

cpu2_2_io1_1ms_RR = [12 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ,
                     12 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ,13 ,12 ,
                     12 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ,
                     13 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ,
                     12 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ,12 ]

io1_1_cpu2_2_1ms_RR = [669 ,562 ,563 ,559 ,559 ,559 ,585 ,564 ,561 ,593 ,
                       562 ,559 ,585 ,559 ,589 ,566 ,556 ,557 ,579 ,560 ,
                       558 ,563 ,552 ,556 ,581 ,561 ,555 ,594 ,568 ,563 ,
                       579 ,569 ,586 ,551 ,565 ,566 ,565 ,593 ,558 ,558 ,
                       554 ,578 ,560 ,574 ,556 ,559 ,582 ,563 ,558 ,560 ]

# Caso 3: 1 cpubench
        #Formato de nombre : cpu{nº cpus}_{nº de cpu medida}_io{nº de ios}_{nº de io medida} 
        # si nº de io/cpu es cero no lo colocamos en el nombre.
cpu1_1_io0_1ms_RR = [ 35 , 35 , 35 , 35 , 35 , 36 , 36 , 35 , 36 , 35 ,
                      35 , 36 , 35 , 35 , 35 , 35 , 35 , 35 , 35 , 35 ,
                      35 , 35 , 35 , 35 , 35 , 35 , 35 , 35 , 35 , 35 ,
                      35 , 35 , 35 , 35 , 35 , 35 , 35 , 35 , 36 , 35 ,
                      35 , 35 , 35 , 35 , 35 , 35 , 35 , 36 , 35 , 35 ]

# Caso 4: 1 cpubench 2 iobench
        #Formato de nombre : cpu{nº cpus}_{nº de cpu medida}_io{nº de ios}_{nº de io medida}
cpu1_1_io2_2_1ms_RR = [19 ,19 ,18 ,19 ,19  ,18 ,19 ,19 ,19 ,19 ,
                        19 ,19 ,19 ,19 ,19 ,19 ,19 ,19 ,18 ,18 ,
                        19 ,18 ,19 ,19 ,19 ,19 ,19 ,19 ,19 ,18 ,
                        18 ,19 ,19 ,18 ,19 ,18 ,19 ,19 ,19 ,19 ,
                        18 ,19 ,19 ,19 ,18 ,18 ,19 ,18 ,18 ,18 ]

io2_1_cpu1_1_1ms_RR = [822,810,772,770,891,866,723,733,824,757,
                       791,823,903,698,867,746,828,643,735,911,
                       749,870,815,987,727,887,810,781,801,750,
                       786,792,746,845,801,811,925,910,691,747,
                       754,857,733,854,868,913,805,926,812,778]

io2_2_cpu1_1_1ms_RR = [761 ,784 ,618 ,683 ,799 ,673 ,696 ,778 ,745 ,714 ,
                        752 ,719 ,677 ,784 ,723 ,733 ,716 ,685 ,635 ,672 ,
                        816 ,807,723 ,759 ,734 ,797 ,813 ,800 ,786 ,793 ,
                        724 ,801 ,671 ,756 ,740 ,734 ,817,623 ,748 ,754 ,
                        780 ,734 ,731 ,680 ,798 ,747,767 ,687 ,745, 816 ]

# Caso 5: 2 cpubench 2 iobench

cpu2_1_io2_2_1ms_RR = [15,16,16,15,16,16,16,16,15,16,
                        16,16,15,16,16,16,15,16,15,16,
                        16,16,16,16,16,15,15,16,15,16,
                        16,16,16,16,16,16,15,15,16,16,
                        16,15,16,16,16,15,16,16,16,15]

cpu2_2_io2_2_1ms_RR = [10,11,11,11,11,11,11,11,
                        11,11,11,11,11,11,11,11,
                        11,11,11,11,11,11,11,11,
                        11,11,11,11,11,11,11,11,
                        11,11,11,11,11,11,11,11,
                        11,11,11,11,11,11,11,11]

io2_1_cpu2_2_1ms_RR = [467,481,436,510,479,438,462,493,455,406,
                        412,564,503,564,531,502,392,582,474,509,
                        435,494,421,456,431,465,490,438,499,402,
                        412,465,491,572,537,435,497,497,560,457,
                        570,571,568,473,450,558,486,417,446,414]

io2_2_cpu2_2_1ms_RR = [347,433,488,431,442,427,361,422,485,382,
                        441,460,482,411,496,503,407,467,419,448,
                        360,446,405,469,374,406,408,468,484,436,
                        440,414 ,496,564,471,464,472,432,530,483,
                        483,524,544,521,419,532,498,253,443,367]

# Caso 6: 2 cpubench

cpu2_1_io0_1ms_RR = [19,20,20,20,20,20,20,20,20,20,
                     21,20,21,21,20,20,20,20,20,20,
                     20,20,20,20,20,20,20,20,20,20,
                     20,20,20,20,20,20,20,20,20,20,
                     20,20,20,20,20,20,20,20,20,20]

cpu2_2_io0_1ms_RR = [20,19,20,20,20,20,20,20,20,20,
                     20,20,20,20,20,20,20,20,20,20,
                     20,20,20,20,20,20,20,20,20,20,
                     20,20,21,20,20,20,20,20,20,20,
                     20,20,20,20,20,20,20,20,20,20]

# Caso 7: 2 iobench

io2_1_cpu0_1ms_RR = [3095,2913,3046,2621,2925,2878,2965,2613,2831,3160,
                     2964,2807,2859,3059,2961,2874,2903,2784,2897,2696,
                     2859,2899,2960,2698,2816,2959,2906,3170,2809,2696,
                     2748,2752,2752,2834,2860,2715,2811,2844,2622,2971,
                     2724,2969,2850,2924,2955,2958,2747,2706,2935,2851]

io2_2_cpu0_1ms_RR = [2947,2969,3061,2618,2891,2710,2947,2611,2977,3130,
                     2841,2735,2744,2959,2961,2996,2785,2836,2657,2818,
                     2866,2657,2878,2779,2891,2868,2932,2936,2686,2774,
                     2778,2706,2674,2837,2793,2652,2778,2801,2638,2816,
                     2793,3027,2978,2730,2764,2781,2911,2768,2845,2801]




def cpubench_1msRR():
    
    cpu2io0_1msRR = [(x+y)/2 for x,y in zip(cpu2_1_io0_1ms_RR,cpu2_2_io0_1ms_RR)]
    cpu2io1_1msRR = [(x+y)/2 for x,y in zip(cpu2_1_io1_1ms_RR,cpu2_2_io1_1ms_RR)]
    cpu2io2_1msRR = [(x+y)/2 for x,y in zip(cpu2_1_io2_2_1ms_RR,cpu2_2_io2_2_1ms_RR)]
    
    cpuμ_1msRR = [np.mean(cpu1_1_io0_1ms_RR),np.mean(cpu1_1_io1_1_1ms_RR),np.mean(cpu1_1_io2_2_1ms_RR),
                       np.mean(cpu2io0_1msRR),np.mean(cpu2io1_1msRR),np.mean(cpu2io2_1msRR)]

    return cpuμ_1msRR

    
def iobench_1msRR():
      
    io2cpu0_1msRR= [(x+y)/2 for x,y in zip(io2_1_cpu0_1ms_RR,io2_2_cpu0_1ms_RR)]
    io2cpu1_1msRR= [(x+y)/2 for x,y in zip(io2_1_cpu1_1_1ms_RR,io2_2_cpu1_1_1ms_RR)]
    io2cpu2_1msRR= [(x+y)/2 for x,y in zip(io2_1_cpu2_2_1ms_RR,io2_2_cpu2_2_1ms_RR)]
    
    ioμ_1msRR = [np.mean(io1_1_cpu0_1ms_RR),np.mean(io1_1_cpu1_1_1ms_RR),np.mean(io2cpu1_1msRR),
                np.mean(io2cpu0_1msRR),np.mean(io1_1_cpu2_2_1ms_RR),np.mean(io2cpu2_1msRR)]

    return ioμ_1msRR

cpuμ_1msRR = cpubench_1msRR()
ioμ_1msRR = iobench_1msRR()
















