tissue_dict = {
    "Achilles tendon": ["Achilles tendon", ],
    "Adipose": ["Adipose",],
    "Adrenal gland": ["Adrenal gland",],
    "Alveolar bone": ["Alveolar bone",],
    "Aorta": ["Aorta",],
    "Bladder": ["Bladder",],
    "Bone": ["Bone",],
    "Bone marrow": ["Bone marrow",],
    "Brain": ["Amygdala", "Anterior cingulate cortex", "Anterior pituitary", "Brain", "Cerebellar Interpositus nucleus",
    "Cerebellum", "Cerebellum cortex", "Cingulate gyrus", "Corpus striatum", "Dorsal hippocampus", "Dorsal striatum",
    "Dorsal subiculum", "Dorsolateral striatum", "Entorhinal cortex", "Forebrain", "Frontal cortex", "Hippocampus",
    "Hypothalamic supraoptic nucleus", "Hypothalamus", "Infralimbic cortex", "Lateral habenula", "Neuroretina",
    "Olfactory bulb", "Orbitofrontal cortex", "Paraventricular nucleus", "Periaqueductal gray", "Pineal gland",
    "Pituitary", "Prefrontal cortex", "Prelimbic cortex", "Preoptic area", "Striatum", "Subcortical white matter",
    "Superficial superior colliculus", "Superficial zone", "Thalamus", "Trigeminal nucleus caudalis",
    "Ventral dentate gyrus", "Ventral tegmental area", "White matter"],
    "Breast": ["Basal fractions", "Breast", "Luminal fractions"],
    "Cartilage": ["Cartilage",],
    "Colon": ["Colon",],
    "Dorsal root ganglia": ["Dorsal root ganglia", "L5"],
    "Ear": ["Middle ear mucosa",],
    "Embryo": ["Embryo",],
    "Eye": ["Eye", "Lens capsule"],
    "Gingiva": ["Gingiva",],
    "Heart": ["Heart",],
    "Kidney": ["Connecting tubule", "Cortex", "Cortical collecting duct", "Cortical thick ascending limb",
    "Descending thin limb of long-loop nephron of inner medulla", "Descending thin limb of short-loop nephron",
    "Distal convoluted tubule", "Glomeruli", "Inner medulla", "Inner medullary collecting duct", "Kidney", "Medulla",
    "Medullary thick ascending limb", "Outer medulla", "Outer medullary collecting duct", "S1 proximal tubule",
    "S2 proximal tubule", "S3 proximal tubule", "Thin ascending limb", "Whole kidney"],
    "Large intestine": ["Large intestine",],
    "Liver": ["Liver",],
    "Lung": ["Lung",],
    "Muscle": ["Extensor digitorum longus", "Gastrocnemius", "Iliopsoas", "Muscle", "Plantaris", "Skeletal muscle",
    "Supraspinatus", "Thyroarytenoid muscle", "Tibialis anterior"],
    "Nerve": ["Sciatic nerve",],
    "Ovary": ["Ovary",],
    "Pancreatic islet": ["Pancreatic islet",],
    "Patellar tendon": ["Patellar tendon",],
    "Penis": ["Penis",],
    "Placenta": ["Placenta",],
    "Plantaris tendon": ["Plantaris tendon",],
    "Prostate": ["Prostate",],
    "Retina": ["Retina",],
    "Salivary gland": ["Salivary gland",],
    "Skin": ["Skin",],
    "Small intestine": ["Small intestine",],
    "Sperm": ["Sperm",],
    "Spinal cord": ["Cervical thoracic lumbar", "Dorsal horn", "Gray matter", "Spinal cord"],
    "Spleen": ["Spleen",],
    "Stomach": ["Stomach",],
    "Testis": ["Testis",],
    "Thymus": ["Thymus",],
    "Trachea": ["Trachea",],
    "Urethral tissue": ["Urethral tissue",],
    "Urogenital sinus": ["Urogenital sinus",],
    "Uterus": ["Endometrium", "Uterine placental interface", "Uterus"],
    "Vagina": ["Vagina",],
    "Whole blood": ["Whole blood",],
    "Yolk sac": ["Yolk sac",],
}
primaryCell_dict = {
    "Alveolar type 2 cell": ["Lung",],
    "Alveolar type-I-like epithelial cell": ["Lung",],
    "Aortic smooth muscle cell": ["Aorta",],
    "Astrocyte": ["Brain",],
    "B cell": ["Spleen",],
    "Brest epithelial cell": ["Breast",],
    "Cardiac fibroblast": ["Heart",],
    "Cardiomyocyte": ["Heart",],
    "CD45+ immune cell": ["Brain",],
    "CD4+ T cell": ["Peripheral blood", "Spinal cord"],
    "Embryonic stem cell": ["Embryo",],
    "Fibroblast-like synoviocyte": ["Synovial tissue",],
    "Germ cell": ["Testis",],
    "Hepatic stellate cell": ["Liver",],
    "Hepatocyte": ["Liver",],
    "Leukocyte": ["Peripheral blood",],
    "Macrophage": ["Bone marrow", "Brain", "Lung", "Peritoneal"],
    "Mesenchymal stem cell": ["Bone marrow",],
    "Microglia": ["Brain", "Retinal", "Spinal cord"],
    "Neural progenitor cell": ["Spinal cord",],
    "Neural stem cell": ["Hippocampus",],
    "Neuron": ["Dorsal root ganglion", "Embryonic cortical neuron", "Hippocampus", "Striatal neuron"],
    "Oligodendrocyte": ["Cerebellum", "Nerve"],
    "Oligodendrocyte precursor cell":["Cerebral cortex",],
    "Oocyte": ["Ovary",],
    "Osteoblast": ["Cranium",],
    "Pancreatic beta cell": ["Pancreas islet",],
    "PBMC": ["Peripheral blood",],
    "Proximal tubule epithelial cell": ["Kidney",],
    "Pyramidal neuron": ["Cortex", "Hippocampus"],
    "Renal tube epithelial cell": ["Kidney",],
    "Retinal ganglion cell": ["Retinal",],
    "Schwann cell": ["Nerve",],
    "Sertoli cell": ["Testis",],
    "T cell": ["Brain parenchyma", "Kidney", "Lung", "Meninges brain", "Peripheral blood"],
    "Theca-interstitial cell": ["Ovarian follicle",],
    "Trophoblast stem cell": ["Embryo",],
    "Vascular endothelial cell": ["Cerebral microvessel", "Liver sinusoidal"],
    "Ventricular myocyte": ["Heart",],
    "White blood cell": ["Blood",]
}
cellLine_list = ["AR42J (Pancreatic acinar carcinoma)", "FRT (Fischer Rat Thyroid epithelial cell line)",
"GH4C1 (Pituitary tumor cell line)", "H9C2 (Embryonic cardiomyoblast cell line)",
"IEC-18 (Normal epithelial cells of the rat ileum)", "INS-1E (Insulinoma β cell line)", "INS-1 (Insulinoma β cell line)",
"N27 (Dopaminergic neuronal cell)", "Odora (Olfactory neuron)", "OLN93 (Oligodendrocytes cell line)", "PAC1 (Pulmonary artery smooth muscle cell line)",
"PAIII (Prostate cancer cell)", "PC12 (Neural crest origin pheochromocytoma)", "PCCL3 (Follicular thyroid cell line)",
"R3327-AT1 (Prostate cancer cell)", "RASMC (Rat aortic smooth muscle cell)", "RBL-2H3 (Basophilic leukemia cell line)",
"Rcho1 (Choriocarcinoma cell line)", "rMC-1 (Retinal Müller cell line)", "RN46A-B14 (Serotonergic neuronal cell line, BDNF-overexpression)",
"RN46A (Serotonergic neuronal cell line)", "RPE-J (Retinal pigment epithelial (RPE) cell line)", "S16 (Primary Schwann cells derived cell line)",
"SIRMu-1 (Immortalized rat Müller-1 cell line)", "Walker-256 (Breast carcinoma cell line)"]
var cellLineFlag = 0;

function addCellLine() {
    var catalogElement = document.getElementById("catalog");
    var select = document.createElement("select");
    select.setAttribute("id", "selectCellLine");
    select.setAttribute("name", "CellLine");
    select.setAttribute("multiple", "multiple");
    select.setAttribute("required", "required");
    select.setAttribute("oninvalid", "setCustomValidity('Please select at least one')")

    for(var i = 0; i < cellLine_list.length; i++) {
        var option = new Option(cellLine_list[i], cellLine_list[i]);
        select.options.add(option);
    }

    catalogElement.appendChild(select);
    $("#selectCellLine").multipleSelect();
}

function chFirst(obj) {
    if(obj.options[obj.selectedIndex].value == "Tissue") {
        document.getElementById("Tissue").style.display = "";
        document.getElementById("selectTissue").style.display = "";
        document.getElementById("selectTissue").value = "All";
        document.getElementById("PrimaryCell").style.display = "none";
        document.getElementById("selectPrimaryCell").style.display = "none";
        document.getElementById("CellLine").style.display = "none";
        if(cellLineFlag == 1) {
            document.getElementById("selectCellLine").remove();
            var ms_parent = document.getElementsByClassName("ms-parent ");
             ms_parent[0].remove();
             cellLineFlag = 0;
        }

        var littleTittle = document.getElementById("littleTittle");
        var sub_select = document.getElementById("sub_select");
        var ms_parent = document.getElementsByClassName("ms-parent ");
        if(littleTittle && sub_select) {
            littleTittle.remove();
            sub_select.remove();
            ms_parent[0].remove();
        }
    }
    else if(obj.options[obj.selectedIndex].value == "PrimaryCell") {
        document.getElementById("PrimaryCell").style.display = "";
        document.getElementById("selectPrimaryCell").style.display = "";
        document.getElementById("selectPrimaryCell").value = "All";
        document.getElementById("Tissue").style.display = "none";
        document.getElementById("selectTissue").style.display = "none";
        document.getElementById("CellLine").style.display = "none";
        if(cellLineFlag == 1) {
            document.getElementById("selectCellLine").remove();
            var ms_parent = document.getElementsByClassName("ms-parent ");
             ms_parent[0].remove();
             cellLineFlag = 0;
        }

        var littleTittle = document.getElementById("littleTittle");
        var sub_select = document.getElementById("sub_select");
        var ms_parent = document.getElementsByClassName("ms-parent ");
        if(littleTittle && sub_select) {
            littleTittle.remove();
            sub_select.remove();
            ms_parent[0].remove();
        }
    }
    else if(obj.options[obj.selectedIndex].value == "CellLine") {
        document.getElementById("Tissue").style.display = "none";
        document.getElementById("selectTissue").style.display = "none";
        document.getElementById("PrimaryCell").style.display = "none";
        document.getElementById("selectPrimaryCell").style.display = "none";
        document.getElementById("CellLine").style.display = "";
        cellLineFlag = 1;

        var littleTittle = document.getElementById("littleTittle");
        var sub_select = document.getElementById("sub_select");
        var ms_parent = document.getElementsByClassName("ms-parent ");
        if(littleTittle && sub_select) {
            littleTittle.remove();
            sub_select.remove();
            ms_parent[0].remove();
        }

        addCellLine();
    }
    else{
        document.getElementById("Tissue").style.display = "none";
        document.getElementById("selectTissue").style.display = "none";
        document.getElementById("PrimaryCell").style.display = "none";
        document.getElementById("selectPrimaryCell").style.display = "none";
        document.getElementById("CellLine").style.display = "none";
        if(cellLineFlag == 1) {
            document.getElementById("selectCellLine").remove();
            var ms_parent = document.getElementsByClassName("ms-parent ");
             ms_parent[0].remove();
             cellLineFlag = 0;
        }

        var littleTittle = document.getElementById("littleTittle");
        var sub_select = document.getElementById("sub_select");
        var ms_parent = document.getElementsByClassName("ms-parent ");
        if(littleTittle && sub_select) {
            littleTittle.remove();
            sub_select.remove();
            ms_parent[0].remove();
        }
    }
}

function addTittle(classification, catalogElement) {
    var littleTittle = document.getElementById("littleTittle");
    var sub_select = document.getElementById("sub_select");
    var ms_parent = document.getElementsByClassName("ms-parent ");
    if(littleTittle && sub_select) {
        littleTittle.remove();
        sub_select.remove();
        ms_parent[0].remove();

    }
    var Sub = document.createElement("strong");
    Sub.id = "littleTittle";
    Sub.style = "font-size=16px;";
    if(classification == "Tissue")
        Sub.innerHTML = "Subtissue: ";
    else if(classification == "PrimaryCell")
        Sub.innerHTML = "Tissue Source: ";
    catalogElement.appendChild(Sub);
}

function addSubSelect(classification, catalogElement, subName) {
    addTittle(classification, catalogElement);
    var select = document.createElement("select");
    select.setAttribute("id", "sub_select");
    select.setAttribute("name", subName);
    select.setAttribute("multiple", "multiple");
    select.setAttribute("required", "required");
    select.setAttribute("oninvalid", "setCustomValidity('Please select at least one')")

    if(subName == "All") {
        var littleTittle = document.getElementById("littleTittle");
        var sub_select = document.getElementById("sub_select");
        var ms_parent = document.getElementsByClassName("ms-parent ");

        littleTittle.remove();
        sub_select.remove();
        ms_parent[0].remove();

    }
    else if(classification == "Tissue") {
        subList = tissue_dict[subName];
        for(var i = 0; i < subList.length; i++) {
            var option = new Option(subList[i], subList[i]);
            select.options.add(option);
        }
    }
    else if(classification == "PrimaryCell") {
        subList = primaryCell_dict[subName];
        for(var i = 0; i < subList.length; i++) {
            var option = new Option(subList[i], subList[i]);
            select.options.add(option);
        }
    }
    catalogElement.appendChild(select);
    $("#sub_select").multipleSelect();
}

function chSecond(obj) {
    var catalogElement = document.getElementById("catalog");
    var subName = obj.options[obj.selectedIndex].value;
    addSubSelect("Tissue", catalogElement, subName);
}

function chThird(obj) {
    var catalogElement = document.getElementById("catalog");
    var subName = obj.options[obj.selectedIndex].value;
    addSubSelect("PrimaryCell", catalogElement, subName);
}
