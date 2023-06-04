FEATURE_SETS = ["Botnet", "DoH", "DoS", "DNS", "TOR", "VPN", "ALL", "COMBO", "COMBO2", "Cryptomining", ]

botnet_best_features = [
 'AVERAGE_DISPERSION',
 'DIRECTIONS',
 'VAR',
 'HURST_EXPONENT',
 'CNT_DISTRIBUTION',
 'SWITCHING_METRIC',
 'MEDIAN',
 'ENTROPY',
 'MIN_POWER',
 'MEDIAN_SCALED_TIME',
 'PACKETS',
 'PACKETS_REV',
 'BYTES',
 'BYTES_REV',
 'DURATION',
]

doh_best_features = [
 'Q1_SCALED_TIME',
 'MEDIAN_DIFFTIMES',
 'BIGGEST_CNT_1_SEC',
 'HURST_EXPONENT',
 'DIRECTIONS',
 'MAX',
 'MIN_MINUS_MAX',
 'FISHER_PEARSON_g1_SKEWNESS',
 'VAL',
 'MODE',
 'PACKETS',
 'PACKETS_REV',
 'BYTES',
 'BYTES_REV',
 'DURATION',
]

dos_best_features = [
 'MEAN_SCALED_DIFFTIMES',
 'MEAN_SCALED_TIME',
 'Q3_SCALED_TIME',
 'BIGGEST_CNT_1_SEC',
 'ENTROPY',
 'P_BENFORD',
 'Q3',
 'MAX',
 'MEDIAN',
 'MIN',
 'PACKETS',
 'PACKETS_REV',
 'BYTES',
 'BYTES_REV',
 'DURATION',
]

dns_malware_features = [
 'DIRECTIONS',
 'CNT_DISTRIBUTION',
 'MEDIAN_SCALED_TIME',
 'GALTON_SKEWNESS',
 'Q1',
 'MEDIAN_DIFFTIMES',
 'MEDIAN',
 'MEAN',
 'P_BENFORD',
 'Q3',
 'PACKETS',
 'PACKETS_REV',
 'BYTES',
 'BYTES_REV',
 'DURATION',
]

tor_features = [
 'MAX_POWER',
 'MEAN_SCALED_TIME',
 'MAX_DIFFTIMES',
 'MEAN',
 'BURSTINESS',
 'ENTROPY',
 'AVERAGE_DISPERSION',
 'SPECTRAL_ENTROPY',
 'Q3',
 'BIGGEST_CNT_1_SEC',
 'PACKETS',
 'PACKETS_REV',
 'BYTES',
 'BYTES_REV',
 'DURATION',
]

vpn_features = [
 'BIGGEST_CNT_1_SEC',
 'DIRECTIONS',
 'SWITCHING_METRIC',
 'HURST_EXPONENT',
 'TRANSIENTS',
 'SPECTRAL_CREST',
 'Q1_SCALED_TIME',
 'MIN_MINUS_MAX',
 'MIN',
 'VAL',
 'TIME',
 'PACKETS',
 'PACKETS_REV',
 'BYTES',
 'BYTES_REV',
 'DURATION',
]

all_best_features = [
 'SWITCHING_METRIC',
 'DIRECTIONS',
 'MIN_MINUS_MAX',
 'Q3',
 'MIN',
 'MEDIAN_DIFFTIMES',
 'SPECTRAL_ENTROPY',
 'P_BENFORD',
 'Q1',
 'VAL',
 'TIME',
 'SPECTRAL_KURTOSIS',
 'PACKETS',
 'PACKETS_REV',
 'BYTES',
 'BYTES_REV',
 'DURATION',
]

combo_features = [
 'MEDIAN',
 'MEAN',
 'MIN_DIFFTIMES',
 'BIGGEST_CNT_1_SEC',
 'VAL',
 'TIME',
 'MODE',
 'P_BENFORD',
 'PERCENT_BELOW_MEAN',
 'Q3',
 'MIN',
 'PACKETS',
 'PACKETS_REV',
 'BYTES',
 'BYTES_REV',
 'DURATION',
]

combo_2_features = [
 'MEDIAN',
 'MEAN',
 'MIN_DIFFTIMES',
 'BIGGEST_CNT_1_SEC',
 'VAL',
 'TIME',
 'MODE',
 'P_BENFORD',
 'MIN',
 'PERCENT_BELOW_MEAN',
 'Q3',
 'PACKETS',
 'PACKETS_REV',
 'BYTES',
 'BYTES_REV',
 'DURATION',
]

crypto_features = [
 'NORMAL_DISTRIBUTION',
 'MAX',
 'MEDIAN',
 'FISHER_MI_3_SKEWNESS',
 'SPECTRAL_CREST',
 'Q1',
 'ROOT_MEAN_SQUARE',
 'SPECTRAL_ENERGY',
 'MIN_DIFFTIMES',
 'DIRECTIONS',
 'PACKETS',
 'PACKETS_REV',
 'BYTES',
 'BYTES_REV',
 'DURATION',
]

def without_flow_header(features):
    _f = []
    for f in features:
        if f in ['PACKETS', 'PACKETS_REV', 'BYTES', 'BYTES_REV']:
            continue
        _f.append(f)
    return _f