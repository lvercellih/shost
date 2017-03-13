from shost import models


def install_dicts(model, dicts, id_field_name='id'):
    all_ids = [x[id_field_name] for x in dicts]
    filters = { id_field_name + '__in': all_ids }
    existent_ids = [x[id_field_name] for x in model.objects.filter(**filters).values(id_field_name)]
    missed_ids = set(all_ids).difference(set(existent_ids))
    insert_objs = [model(**x) for x in dicts if x[id_field_name] in missed_ids]
    model.objects.bulk_create(insert_objs)


def create_if_not_exist(model, filters, data):
    if model.objects.filter(**filters).count() == 0:
        model.objects.create(**data)


def create_all_if_not_exist(model, list):
    for item in list:
        create_if_not_exist(model, *item)


def install_entity_classes(dicts):
    install_dicts(models.EClass, dicts)


def install_entity_statuses(dicts):
    install_dicts(models.Status, dicts)


def install_operations(dicts):
    install_dicts(models.Operation, dicts)
