class Solution:
	def minEatingSpeed(self, piles: List[int], h: int) -> int:

		def check_speed(speed, hour):

			total_hour = 0

			for pile in piles:
				exact_pile = pile // speed
				extra_pile = pile % speed

				if extra_pile > 0:
					total_hour = total_hour + exact_pile + 1
				else:
					total_hour = total_hour + exact_pile

			if total_hour <= hour:
				return True
			else:
				return False

		min_speed , max_speed = 1 , (10**9)+1

		while min_speed < max_speed:

			mid = (min_speed + max_speed) // 2

			if check_speed(mid , h) == True:
				max_speed = mid
			else:
				min_speed = mid + 1

		return min_speed
