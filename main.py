import sys
from recall import run_mock_recall, export_recall_report


def main():
    # Check input arguments
    if len(sys.argv) != 2:
        print("Usage: python main.py <FINISHED_LOT_ID>")
        print("Example: python main.py F500")
        sys.exit(1)

    finished_lot_id = sys.argv[1]

    try:
        print(f"Starting mock recall for finished lot: {finished_lot_id}")

        recall_report = run_mock_recall(finished_lot_id)
        export_recall_report(recall_report)

        print("Mock recall completed successfully.")
        print(f"Batch ID: {recall_report['batch_id']}")
        print(f"Impacted customers: {recall_report['impacted_customers']}")
        print(f"Total quantity affected: {recall_report['total_quantity']}")
        print(f"Recall time (s): {recall_report['recall_time_seconds']}")

        print("Reports generated in /output folder.")

    except Exception as e:
        print("ERROR during mock recall execution:")
        print(str(e))
        sys.exit(2)


if __name__ == "__main__":
    main()
