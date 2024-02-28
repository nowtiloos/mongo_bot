from shemas.shemas import SDataIn, SDataOut


class MongoDBAggregator:
    def __init__(self, collection_name) -> None:
        self.collection = collection_name

    def aggregate_data_by_time(self, query: SDataIn) -> SDataOut:
        match_stage = {
            "$match": {"dt": {"$gte": query.dt_from, "$lte": query.dt_upto}}
        }

        grouping_expression = {
            "hour": {"$hour": "$dt"},
            "day": {"$dayOfYear": "$dt"},
            "month": {"$month": "$dt"}
        }

        group_stage = {
            "$group": {
                "_id": grouping_expression[query.group_type],
                "labels": {"$first": "$dt"},
                "total": {"$sum": "$value"}
            }
        }

        sort_stage = {"$sort": {"labels": 1}}

        pipeline: list = [match_stage, group_stage, sort_stage]

        result = tuple(self.collection.aggregate(pipeline))

        dataset = [entry["total"] for entry in result]
        labels = [entry["labels"] for entry in result]

        return SDataOut(dataset=dataset, labels=labels)
