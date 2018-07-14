CPP_FILES := $(shell find . -name "*.cpp")
TARGETS := $(CPP_FILES:.cpp=.out)
all: $(TARGETS)

%.out: %.cpp
	$(CXX) -std=c++17 -o $@ $<

clean:
	rm *.out