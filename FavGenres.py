'''
Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the user has listened to as values.

Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs within that genre as values. The song can only belong to only one genre.

The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list of the user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one favorite genre if he/she has listened to the same number of songs per each of the genres.

Example 1:

Input:
userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
},
songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

Output: {  
   "David": ["Rock", "Techno"],
   "Emma":  ["Pop"]
}

Explanation:
David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.

'''
import collections
def mapSong_Genre(song: str, genre:{}) -> str:
	for genreName, songList in genre.items():
		if song in songList:
			return genreName

def favGenres(users:{}, genre:{}) -> {}:
	# map each song to genre
	user_genre_dict, op = {}, []
	for userName, songList in users.items():
		user_genre_dict[userName] = [mapSong_Genre(song, genre) for song in songList]
		# count genre and get most frequent
		# cnt_bucket, maxValue = {}, float('-inf')
		# for gen in user_genre_dict[userName]:
		# 	cnt_bucket.setdefault(gen, 0)
		# 	cnt_bucket[gen] += 1
		# 	maxValue = max(maxValue, cnt_bucket[gen])
		cnt_bucket = collections.Counter(user_genre_dict[userName])
		maxValue = max(cnt_bucket.values())
		# append to output the most common for each user
		op.append({userName: [genreName for genreName, genreCount in cnt_bucket.items() if genreCount == maxValue]})
		# op.append({userName: [genreName for genreName, genreCount in cnt_bucket.items() if genreCount==maxValue]})

	# return op
	return op

userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}
songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

res = favGenres(userSongs, songGenres)
print(res)