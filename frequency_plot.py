def plot(freqs, PLOT_HEIGHT=20):
    freqs = [(k, freqs[k]) for k in sorted(freqs.keys())]
    max_freq = max([y for (x, y) in freqs])
    step = max_freq/PLOT_HEIGHT
    for i in range(PLOT_HEIGHT):
        print(end='{:.3f} |'.format(max_freq))
        for (x, y) in freqs:
            if y >= max_freq:
                print(end='█ ')
            else:
                print(end='  ')
        max_freq -= step
        print()
    print('       ----------------------------------------------------')
    print('       A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
