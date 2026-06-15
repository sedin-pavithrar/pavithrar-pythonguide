# Doubly Linked List where each node holds song name, artist, and duration. Supports add_song 
# (append), remove_current (unlink with pointer update), next_track, prev_track with boundary 
# messages, and show_queue that marks the current node. This is exactly the internal structure 
# Spotify uses for its queue.
# Problem
# Doubly Linked List playlist: add song, remove current, next/prev track, display queue with  [playing] marker.
# Constraints
# next_track() on last -> "End of playlist"
# prev_track() on first -> "Already at beginning"
# Duration displays in mm:ss
# Bonus: Add shuffle() that randomises playlist order.


class SongNode:

    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration

        self.prev = None
        self.next = None 


class Playlist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, name, artist, duration):

        new_song = SongNode(name, artist, duration)

        # Empty playlist
        if self.head is None:
            self.head = new_song
            self.tail = new_song
            self.current = new_song
            return

        self.tail.next = new_song
        new_song.prev = self.tail
        self.tail = new_song

    def next_track(self):

        if  self.playlist_empty():
            return 

        if self.current.next is None:
            print(" End of playlist ")
            return

        self.current = self.current.next
        self.show_current()

    def prev_track(self):

        if self.playlist_empty():
            return

        if self.current.prev is None:
            print(" Already at first song ")
            return

        self.current = self.current.prev
        self.show_current()

    def remove_current(self):
        if self.playlist_empty():
            return

        removed = self.current

        # Only one song
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.current = None

        # Removing first song
        elif removed == self.head:
            self.head = removed.next
            self.head.prev = None
            self.current = self.head

        # Removing last song
        elif removed == self.tail:
            self.tail = removed.prev
            self.tail.next = None
            self.current = self.tail

        # Removing middle song
        else:
            removed.prev.next = removed.next
            removed.next.prev = removed.prev
            self.current = removed.next

        print(f" Removed: {removed.name}")

    def playlist_empty(self):
        if self.head is None:
            print(" Playlist is empty ")
            return True
        
        return False
    
    def show_current(self):
        if self.playlist_empty():
            return
        
        print(f" Now playing: {self.current.name}")
    
       

    def show_queue(self):

        if self.playlist_empty():
            return

        temp = self.head

        while temp:

            marker = " [playing]" if temp == self.current else ""
            print( f" {temp.name} - {temp.artist} ({temp.duration}s){marker} ")
            temp = temp.next


def main():

    playlist = Playlist()

    playlist.add_song("Believer", "Imagine Dragons", 204)
    playlist.add_song("Shape of You", "Ed Sheeran", 233)
    playlist.add_song("Perfect", "Ed Sheeran", 260)

    playlist.show_queue()

    print("\n --- Next Track ---")
    playlist.next_track()

    print("\n --- Queue ---")
    playlist.show_queue()

    print("\n --- Remove Current ---")
    playlist.remove_current()

    print("\n --- Queue ---")
    playlist.show_queue()

    print("\n --- Previous Track ---")
    playlist.prev_track()
 
    playlist.show_queue()


if __name__ == "__main__":
    main()