from triple_extraction import *


if __name__ == '__main__':
    content = '李克强总理今天来我家了,我感到非常荣幸'
    extractor = TripleExtractor()
    svos = extractor.triples_main(content)
    print('svos', svos)
