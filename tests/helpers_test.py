import unittest

from helpers.flow_helpers import get_queue_name, _convert_class_to_kebab

class FakeStj:
    pass

class FakeTjmg:
    pass

class FakeTjsp:
    pass

class FakeBolsaFamilia:
    pass

class FakeMunicipioBauru:
    pass

class FakeTribunalRegional:
    pass

class TestSetup(unittest.TestCase):
    def test_should_convert_camel_case_to_kebab(self):
        camel_case_names = [
            'STJ',
            'TJMG',
            'TJSP',
            'BolsaFamilia',
            'MunicipioBauru',
            'TribunalRegional'
        ]

        expected_kebab_names = [
            'stj',
            'tjmg',
            'tjsp',
            'bolsa-familia',
            'municipio-bauru',
            'tribunal-regional'
        ]

        for name_index in range(len(camel_case_names)):
            converted_name = _convert_class_to_kebab(camel_case_names[name_index])
            self.assertEqual(converted_name, expected_kebab_names[name_index])

    def test_should_create_queue_name(self):
        classes = [
            FakeStj,
            FakeTjmg,
            FakeTjsp,
            FakeBolsaFamilia,
            FakeMunicipioBauru,
            FakeTribunalRegional
        ]

        expected_queue_names = [
            'fake-stj.inputs',
            'fake-tjmg.inputs',
            'fake-tjsp.inputs',
            'fake-bolsa-familia.inputs',
            'fake-municipio-bauru.inputs',
            'fake-tribunal-regional.inputs'
        ]

        for name_index in range(len(classes)):
            queue_name = get_queue_name(
                class_name=classes[name_index].__name__,
                queue_type="inputs"
            )
            self.assertEqual(expected_queue_names[name_index], queue_name)

        
if __name__ == '__main__':
    unittest.main()