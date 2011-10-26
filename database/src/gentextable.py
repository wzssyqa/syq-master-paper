#! /usr/bin/env python
# -*- coding: utf-8 -*-

def do_table(data, line, chi, en):
	f=open('tex.table','a')
	f.write('\\begin{table}[!htbp] \n\\begin{center}\n')
	f.write('\\bicaption{表}{'+chi+'}{Table.}{'+en+'}\n')
	f.write('\\begin{tabular}{lccclccc} \n \\toprule \n')
	f.write('& 相关系数   & 互信息    &灰关联度 \\\\ \n')
	f.write('\\midrule \n')
	for i in range(0, line):
		f.write('独立成分'+str(i+1)+'	& '+str(data[0][i])+'	')
		f.write('& '+str(data[1][i])+'	')
		f.write('& '+str(data[2][i])+'	\\\\ \n')
	f.write('\\bottomrule \n \\end{tabular} \n' +
			'\\end{center} \n \\end{table} \n\n\n')
	f.close()



def gen_ica_tables(mo1_tmp_vs_ica, mo2_tmp_vs_ica, 
		mo1_day_vs_ica, mo2_day_vs_ica, 
		mo1_load_vs_ica, mo2_load_vs_ica
		):
	f=open('tex.table','w')
	f.close()
	do_table(mo1_tmp_vs_ica,4,
		'直接使用FastICA得到的独立成分与气温之间的关系(一号末煤仓)',
		'Relationship between Temperature and ICs from FastICA directly, No.1 of Powder Bulker'
		)
	do_table(mo2_tmp_vs_ica,4,
		'直接使用FastICA得到的独立成分与气温之间的关系(二号末煤仓)',
		'Relationship between Temperature and ICs from FastICA directly, No.2 of Powder Bulker'
		)
	do_table(mo1_day_vs_ica,4,
		'直接使用FastICA得到的独立成分与时间之间的关系(一号末煤仓)',
		'Relationship between Days and ICs from FastICA directly, No.1 of Powder Bulker'
		)
	do_table(mo2_day_vs_ica,4,
		'直接使用FastICA得到的独立成分与时间之间的关系(二号末煤仓)',
		'Relationship between Days and ICs from FastICA directly, No.2 of Powder Bulker'
		)
	do_table(mo1_load_vs_ica,4,
		'直接使用FastICA得到的独立成分与装载量之间的关系(一号末煤仓)',
		'Relationship between Loading and ICs from FastICA directly, No.1 of Powder Bulker'
		)
	do_table(mo1_load_vs_ica,4,
		'直接使用FastICA得到的独立成分与装载量之间的关系(二号末煤仓)',
		'Relationship between Loading and ICs from FastICA directly, No.2 of Powder Bulker'
		)

def gen_pca_tables(mo1_tmp_vs_pca, mo2_tmp_vs_pca, 
		mo1_day_vs_pca, mo2_day_vs_pca, 
		mo1_load_vs_pca, mo2_load_vs_pca
		):
	do_table(mo1_tmp_vs_pca,3,
		'PCA降维后使用FastICA得到的独立成分与气温之间的关系(一号末煤仓)',
		'Relationship between Temperature and ICs from FastICA after PCA, No.1 of Powder Bulker'
		)
	do_table(mo2_tmp_vs_pca,3,
		'PCA降维后使用FastICA得到的独立成分与气温之间的关系(二号末煤仓)',
		'Relationship between Temperature and ICs from FastICA after PCA, No.2 of Powder Bulker'
		)
	do_table(mo1_day_vs_pca,3,
		'PCA降维后使用FastICA得到的独立成分与时间之间的关系(一号末煤仓)',
		'Relationship between Days and ICs from FastICA after PCA, No.1 of Powder Bulker'
		)
	do_table(mo2_day_vs_pca,3,
		'PCA降维后使用FastICA得到的独立成分与时间之间的关系(二号末煤仓)',
		'Relationship between Days and ICs from FastICA after PCA, No.2 of Powder Bulker'
		)
	do_table(mo1_load_vs_pca,3,
		'PCA降维后使用FastICA得到的独立成分与装载量之间的关系(一号末煤仓)',
		'Relationship between Loading and ICs from FastICA after PCA, No.1 of Powder Bulker'
		)
	do_table(mo1_load_vs_pca,3,
		'PCA降维后使用FastICA得到的独立成分与装载量之间的关系(二号末煤仓)',
		'Relationship between Loading and ICs from FastICA after PCA, No.2 of Powder Bulker'
		)



