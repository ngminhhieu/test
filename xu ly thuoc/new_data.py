ten_thuoc = ['a_cadimin', 'a_magnesi', 'a_scanneuron', 'a_zoloft', 'a_biotin',
            'a_moc_hoa_trang', 'a_berberin', 'a_tiffy', 'a_augmentin', 'a_terpin_codein',
            'a_alprazolam', 'a_feburic', 'a_aecysmux', 'a_ferricure', 'a_laroxyl', 'a_lincomycin',
            'a_eugica', 'a_tesafu', 'a_dopharalgic', 'thuoc_nhiet_mieng', 'a_teburap', 'a_aerius',
            'a_vitamin_c_tw3', 'a_spirastad', 'a_acetazolamid', 'a_glotadol_f', 'a_loperamid',
            'a_neurobion', 'a_efferalgan', 'a_ban_dau_thong', 'a_metronidazol', 'a_new_ameflu_daytime_vitamin_c',
            'a_colchicin_1mg', 'a_phaanedol', 'a_tanamisolblue', 'a_cam_xuyen_huong', 'a_moxilen',
            'a_rutinc_bcomplex', 'a_bineurox', 'a_amoxicillin', 'a_ameflu_daytime', 'a_biseptol', 'a_alpha_choay',
            'a_xyzal', 'a_ambron_30mg', 'a_singulair_5mg', 'a_bngreen', 'a_an_thao', 'a_3b_medi', 'a_medrol_16mg',
            'a_luc_vi_f', 'a_panadol_extra', 'a_ameflu_nighttime', 'a_alaxan', 'a_nonzoli', 'a_acehasan_200']

ten_thuoc_copy = ['a_zoloft', 'a_biotin',
            'a_moc_hoa_trang', 'a_berberin', 'a_tiffy', 'a_augmentin', 'a_terpin_codein',
            'a_alprazolam', 'a_feburic', 'a_aecysmux', 'a_ferricure', 'a_laroxyl', 'a_lincomycin',
            'a_eugica', 'a_tesafu', 'a_dopharalgic', 'thuoc_nhiet_mieng', 'a_teburap', 'a_aerius',
            'a_vitamin_c_tw3', 'a_spirastad', 'a_acetazolamid', 'a_glotadol_f', 'a_loperamid',
            'a_neurobion', 'a_efferalgan', 'a_ban_dau_thong', 'a_metronidazol', 'a_new_ameflu_daytime_vitamin_c',
            'a_colchicin_1mg', 'a_phaanedol', 'a_tanamisolblue', 'a_cam_xuyen_huong', 'a_moxilen',
            'a_rutinc_bcomplex', 'a_bineurox', 'a_amoxicillin', 'a_ameflu_daytime', 'a_biseptol', 'a_alpha_choay',
            'a_xyzal', 'a_ambron_30mg', 'a_singulair_5mg', 'a_bngreen', 'a_an_thao', 'a_3b_medi', 'a_medrol_16mg',
            'a_luc_vi_f', 'a_panadol_extra', 'a_ameflu_nighttime', 'a_alaxan', 'a_nonzoli', 'a_acehasan_200']

tt = str(ten_thuoc_copy)
tt = tt.replace('[', '(')
tt = tt.replace(']', ')')
tt = tt.replace("\',","\'),")
tt = tt.replace(", \'", ",(\'")
print(len(ten_thuoc))