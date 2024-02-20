class Cache:
    def __init__(self, cache_size, line_size, num_lines_per_set):
        self.cache_size = cache_size
        self.line_size = line_size
        self.num_lines_per_set = num_lines_per_set
        self.num_sets = self.cache_size // (self.line_size * self.num_lines_per_set)
        self.cache = [[(None, False) for _ in range(self.num_lines_per_set)] for _ in range(self.num_sets)]
        self.fifo = [[] for _ in range(self.num_sets)]

    def access_memory(self, address):
        block_number, set_index, tag = self._parse_address(address)

        if self._is_hit(set_index, tag):
            return "HIT"
        else:
            self._update_cache(set_index, tag)
            return "MISS"

    def _parse_address(self, address):
        block_offset = address % self.line_size
        set_index = (address // self.line_size) % self.num_sets
        tag = address // (self.line_size * self.num_sets)
        return block_offset, set_index, tag

    def _is_hit(self, set_index, tag):
        return tag in [line[0][0] for line in self.cache[set_index] if line[1]]

    def _update_cache(self, set_index, tag):
        if None in [line[0] for line in self.cache[set_index]]:
            empty_line_index = [line[0] for line in self.cache[set_index]].index(None)
            self.cache[set_index][empty_line_index] = ((tag,), True)
            self.fifo[set_index].append(empty_line_index)
        else:
            line_to_replace = self.fifo[set_index].pop(0)
            self.cache[set_index][line_to_replace] = ((tag,), True)

def simulate_cache(cache_size, line_size, num_lines_per_set, memory_accesses):
    cache = Cache(cache_size, line_size, num_lines_per_set)
    hits = 0
    misses = 0

    with open(memory_accesses, 'r') as file:
        for line in file:
            address = int(line.strip(), 16)
            result = cache.access_memory(address)
            if result == "HIT":
                hits += 1
            else:
                misses += 1

            cache_output(cache)

    return hits, misses

def cache_output(cache):
    print("=" * 16)
    for set_index, cache_set in enumerate(cache.cache):
        print(f"IDX V ** ADDR **")
        for line_index, line in enumerate(cache_set):
            tag = line[0][0] if line[1] else ""
            valid_bit = "1" if line[1] else "0"
            tag_hex = f"{tag:#010x}" if line[1] else ""
            print(f"{set_index:03d} {valid_bit} {tag_hex}")
    print("=" * 16)


# Exemplo de uso
cache_size = 4096  # 4KB
line_size = 1024    # 1KB
num_lines_per_set = 4  # 4 linhas por conjunto
memory_accesses_file = "memory_accesses.txt"  # Arquivo com os acessos à memória

hits, misses = simulate_cache(cache_size, line_size, num_lines_per_set, memory_accesses_file)
print(f"#hits: {hits}")
print(f"#miss: {misses}")