import factory
from product.models import Brand, Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: "test_category_%d" % n)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: "test_brand_%d" % n)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: "test_product_%d" % n)
    description = factory.Sequence(lambda n: "test_tescription_%d" % n)
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
