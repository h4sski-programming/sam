from django.test import TestCase

# Create your tests here.

from sam_app.models import Module

class ModuleTestCase(TestCase):
    def setUp(self):
        Module.objects.create(name='first', status=True)
        Module.objects.create(name='second', status=True)
        Module.objects.create(name='third', status=False)
        Module.objects.create(name='tourth', status=False)
    
    
    def test_modules(self):
        modules_active = Module.objects.filter(status=True)
        modules_not_active = Module.objects.filter(status=False)
        self.assertEqual(len(modules_active), 2)
        self.assertEqual(len(modules_not_active), 2)
    
    
    def test_change_status(self):
        module_1 = Module.objects.get(name='first')
        module_2 = Module.objects.get(name='second')
        module_3 = Module.objects.get(name='third')
        
        # Checking status before change
        self.assertEqual(module_2.status, module_1.status)
        self.assertNotEqual(module_2.status, module_3.status)
        
        module_2.status = False
        
        # Checkind status after change
        self.assertNotEqual(module_2.status, module_1.status)
        self.assertEqual(module_2.status, module_3.status)
        
    
        