def cartwheel(debug=False):
    soma = h.Section() # one compartment of about 29000 um2
    soma.nseg = 1
    soma.diam = 96
    soma.L = 96
    cm = 1
    v_potassium = -80       # potassium reversal potential
    v_sodium = 50           # sodium reversal potential

    seg = soma
    seg.insert('naRsg')
    seg.insert('kpkj')
    seg.insert('kpkj2')
    seg.insert('kpkjslow')
    seg.insert('bkpkj')
    seg.insert('kpksk')
    seg.insert('cadiff')
    seg.insert('cap')
    seg.insert('lkpkj')
    seg.insert('hpkj')
    seg.ena = 60
    seg.ek = -80
    s = soma()
    s.kpksk.gbar = 0.002
    if not runQuiet:
        print "<< cartwheel: Raman Purkinje cell model (modified) created >>"
    return(soma)
