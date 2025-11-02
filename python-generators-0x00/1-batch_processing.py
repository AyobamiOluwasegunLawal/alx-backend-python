from typing import Generator, List, Dict, Any
import sys

def stream_users_in_batches(batch_size: int) -> Generator[List[Dict[str, Any]], None, None]:
	"""
	Generator that yields batches of users from the user_data table.
	Each batch is a list of dicts, batch_size per batch (except possibly last).
	"""
	seed = __import__('seed')
	conn = None
	cursor = None
	try:
		conn = seed.connect_to_prodev()
		cursor = conn.cursor(dictionary=True)
		cursor.execute("SELECT user_id, name, email, age FROM user_data")
		batch = []
		for row in cursor:
			batch.append(row)
			if len(batch) == batch_size:
				yield batch
				batch = []
		if batch:
			yield batch
	finally:
		try:
			if cursor is not None:
				cursor.close()
		except Exception:
			pass
		try:
			if conn is not None:
				conn.close()
		except Exception:
			pass

def batch_processing(batch_size: int) -> Generator[List[Dict[str, Any]], None, None]:
	"""
	Processes each batch to filter users over the age of 25.
	Yields lists of users (dicts) where age > 25, batch by batch.
	"""
	for batch in stream_users_in_batches(batch_size):
		filtered = [user for user in batch if float(user['age']) > 25]
		if filtered:
			yield filtered

if __name__ == '__main__':
	# Example usage: print batches of users over age 25
	for i, batch in enumerate(batch_processing(5)):
		print(f"Batch {i+1}:")
		for user in batch:
			print(user)
		print()
		if i >= 2:
			break
