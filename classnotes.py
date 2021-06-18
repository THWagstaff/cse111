#def main():
    make_periodic_table
    tables = make_periodic_table()
    for i, line in enumerate(tables):
        print(tables)

def make_periodic_table ():
    table = [ 
        # [symbol, name, atomic_mas]
        {"symbol": "Ac",	"Actinium",	227],
        {"symbol": "Ag",	"Silver",	107.8682],
        {"symbol": "Al",	"Aluminum",	26.9815386],
        {"symbol": "Am",	"Americium",	243],
        {"symbol": "Ar",	"Argon",	39.948],
        {"symbol": "As",	"Arsenic",	74.9216],
        {"symbol": "At",	"Astatine",	210],
        {"symbol": "Au",	"Gold",	196.966569],
        {"symbol": "B",	"Boron",	10.811],
        {"symbol": "Ba",	"Barium",	137.327],
        {"symbol": "Be",	"Beryllium",	9.012182],
        {"symbol": "Bh",	"Bohrium",	272],
        {"symbol": "Bi",	"Bismuth",	208.9804],
        {"symbol": "Bk",	"Berkelium",	247],
        {"symbol": "Br",	"Bromine",	79.904],
        {"symbol": "C",	"Carbon",	12.0107],
        {"symbol": "Ca",	"Calcium",	40.078],
        {"symbol": "Cd",	"Cadmium",	112.411],
        {"symbol": "Ce",	"Cerium",	140.116],
        {"symbol": "Cf",	"Californium",	251],
        {"symbol": "Cl",	"Chlorine",	35.453],
        {"symbol": "Cm",	"Curium",	247],
        {"symbol": "Cn",	"Copernicium",	285],
        {"symbol": "Co",	"Cobalt",	58.933195],
        {"symbol": "Cr",	"Chromium",	51.9961],
        {"symbol": "Cs",	"Cesium",	132.9054519],
        {"symbol": "Cu",	"Copper",	63.546],
        {"symbol": "Db",	"Dubnium",	268],
        {"symbol": "Ds",	"Darmstadtium",	281],
        {"symbol": "Dy",	"Dysprosium",	162.5],
        {"symbol": "Er",	"Erbium",	167.259],
        {"symbol": "Es",	"Einsteinium",	252],
        {"symbol": "Eu",	"Europium",	151.964],
        {"symbol": "F",	"Fluorine",	18.9984032],
        {"symbol": "Fe",	"Iron",	55.845],
        {"symbol": "Fl",	"Flerovium",	289],
        {"symbol": "Fm",	"Fermium",	257],
        {"symbol": "Fr",	"Francium",	223],
        {"symbol": "Ga",	"Gallium",	69.723],
        {"symbol": "Gd",	"Gadolinium",	157.25],
        {"symbol": "Ge",	"Germanium",	72.64],
        {"symbol": "H",	"Hydrogen",	1.00794],
        {"symbol": "He",	"Helium",	4.002602],
        {"symbol": "Hf",	"Hafnium",	178.49],
        {"symbol": "Hg",	"Mercury",	200.59],
        {"symbol": "Ho",	"Holmium",	164.93032],
        {"symbol": "Hs",	"Hassium",	270],
        {"symbol": "I",	"Iodine",	126.90447],
        {"symbol": "In",	"Indium",	114.818],
        {"symbol": "Ir",	"Iridium",	192.217],
        {"symbol": "K",	"Potassium",	39.0983],
        {"symbol": "Kr",	"Krypton",	83.798],
        {"symbol": "La",	"Lanthanum",	138.90547],
        {"symbol": "Li",	"Lithium",	6.941],
        {"symbol": "Lr",	"Lawrencium",	262],
        {"symbol": "Lu",	"Lutetium",	174.9668],
        {"symbol": "Lv",	"Livermorium",	293],
        {"symbol": "Mc",	"Moscovium",	288],
        {"symbol": "Md",	"Mendelevium",	258],
        {"symbol": "Mg",	"Magnesium",	24.305],
        {"symbol": "Mn",	"Manganese",	54.938045],
        {"symbol": "Mo",	"Molybdenum",	95.96],
        {"symbol": "Mt",	"Meitnerium",	276],
        {"symbol": "N",	"Nitrogen",	14.0067],
        {"symbol": "Na",	"Sodium",	22.98976928],
        {"symbol": "Nb",	"Niobium",	92.90638],
        {"symbol": "Nd",	"Neodymium",	144.242],
        {"symbol": "Ne",	"Neon",	20.1797],
        {"symbol": "Nh",	"Nihonium",	284],
        {"symbol": "Ni",	"Nickel",	58.6934],
        {"symbol": "No",	"Nobelium",	259],
        {"symbol": "Np",	"Neptunium",	237],
        {"symbol": "O",	"Oxygen",	15.9994],
        {"symbol": "Og",	"Oganesson",	294],
        {"symbol": "Os",	"Osmium",	190.23],
        {"symbol": "P",	"Phosphorus",	30.973762],
        {"symbol": "Pa",	"Protactinium",	231.03588],
        {"symbol": "Pb",	"Lead",	207.2],
        {"symbol": "Pd",	"Palladium",	106.42],
        {"symbol": "Pm",	"Promethium",	145],
        {"symbol": "Po",	"Polonium",	209],
        {"symbol": "Pr",	"Praseodymium",	140.90765],
        {"symbol": "Pt",	"Platinum",	195.084],
        {"symbol": "Pu",	"Plutonium",	244],
        {"symbol": "Ra",	"Radium",	226],
        {"symbol": "Rb",	"Rubidium",	85.4678],
        {"symbol": "Re",	"Rhenium",	186.207],
        {"symbol": "Rf",	"Rutherfordium",	267],
        {"symbol": "Rg",	"Roentgenium",	280],
        {"symbol": "Rh",	"Rhodium",	102.9055],
        {"symbol": "Rn",	"Radon",	222],
        {"symbol": "Ru",	"Ruthenium",	101.07],
        {"symbol": "S",	"Sulfur",	32.065],
        {"symbol": "Sb",	"Antimony",	121.76],
        {"symbol": "Sc",	"Scandium",	44.955912],
        {"symbol": "Se",	"Selenium",	78.96],
        {"symbol": "Sg",	"Seaborgium",	271],
        {"symbol": "Si",	"Silicon",	28.0855],
        {"symbol": "Sm",	"Samarium",	150.36],
        {"symbol": "Sn",	"Tin",	118.71],
        {"symbol": "Sr",	"Strontium",	87.62],
        {"symbol": "Ta",	"Tantalum",	180.94788],
        {"symbol": "Tb",	"Terbium",	158.92535],
        {"symbol": "Tc",	"Technetium",	98],
        {"symbol": "Te",	"Tellurium",	127.6],
        {"symbol": "Th",	"Thorium",	232.03806],
        {"symbol": "Ti",	"Titanium",	47.867],
        {"symbol": "Tl",	"Thallium",	204.3833],
        {"symbol": "Tm",	"Thulium",	168.93421],
        {"symbol": "Ts",	"Tennessine",	294],
        {"symbol": "U",	"Uranium",	238.02891],
        {"symbol": "V",	"Vanadium",	50.9415],
        {"symbol": "W",	"Tungsten",	183.84],
        {"symbol": "Xe",	"Xenon",	131.293],
        {"symbol": "Y",	"Yttrium",	88.90585],
        {"symbol": "Yb",	"Ytterbium",	173.054],
        {"symbol": "Zn",	"Zinc",	65.38],
        {"symbol": "Zr",	"Zirconium",	91.224],
        ]
    return table

#sum = 0
#for i, value in enumerate(table):
#    value["mass"] = 1
#    if(value["symbol"]) == "nb"):
#        print(value)
#
#    sum += value.get("mass")




students = {"name": "jon",
            "lastName": "smith",
            "address": "1 road street",
            "email": "1@byui.edu"
            }
print(students)

for i in students:
        print(i + ": " + students.get(i))


#if __name__ == "__main__":
#    main()